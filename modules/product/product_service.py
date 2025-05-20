from .product_model import UserDeviceDao


class UserDeviceService:

    def add_device(user_id, device_data):
        return UserDeviceDao.create_device( user_id, device_data)


