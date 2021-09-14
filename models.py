from flask_restful import Resource, reqparse, fields, marshal_with, abort
import datetime


def Order(api, db, date_format):
    class OrdersModel(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100), nullable=False)
        date = db.Column(db.Integer, nullable=False)

        def __repr__(self):
            return f"Orders(name = {self.name},date={self.date})"

    # db.create_all()  # run once, db creation

    orders_put_args = reqparse.RequestParser()
    orders_put_args.add_argument(
        "id", type=int, help="ID of the order is required", required=True)
    orders_put_args.add_argument(
        "name", type=str, help="name of the order is required", required=True)
    orders_put_args.add_argument(
        "date", type=str, help="date of the order is required", required=True)

    resource_fields = {
        'id': fields.Integer,
        'name': fields.String,
        'date': fields.String
    }

    class Orders(Resource):
        @marshal_with(resource_fields)
        def get(self, order_date):
            result = OrdersModel.query.filter_by(date=order_date).all()
            try:
                datetime.datetime.strptime(order_date, date_format)
            except ValueError:
                abort(
                    400, message="date format wrong, make sure date format is DD-MM-YYYY  as string"
                )
            if not result:
                abort(
                    404, message="could not find any orders in this day")
            return result

        @marshal_with(resource_fields)
        def put(self, order_id):
            args = orders_put_args.parse_args()
            result = OrdersModel.query.filter_by(id=order_id).all()
            if result:
                abort(409, message="order id already taken.")
            order = OrdersModel(
                id=order_id, name=args['name'], date=args['date'])
            db.session.add(order)
            db.session.commit()
            return order, 201

    api.add_resource(Orders, "/order/<int:order_id>",
                     "/order/<string:order_date>")
