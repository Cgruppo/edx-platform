""" Constants for this app as well as the external API. """


class OrderStatus(object):
    """Constants representing all known order statuses. """
    OPEN = 'Open'
    ORDER_CANCELLED = 'Order Cancelled'
    BEING_PROCESSED = 'Being Processed'
    PAYMENT_CANCELLED = 'Payment Cancelled'
    PAID = 'Paid'
    FULFILLMENT_ERROR = 'Fulfillment Error'
    COMPLETE = 'Complete'
    REFUNDED = 'Refunded'


class Messages(object):
    """ Strings used to populate response messages. """
    NO_ECOM_API = u'E-Commerce API not setup. Enrolled {username} in {course_id} directly.'
    NO_SKU_ENROLLED = u'The {enrollment_mode} mode for {course_id} does not have a SKU. Enrolling {username} directly.'
    ORDER_COMPLETED = u'Order {order_number} was completed.'
    ORDER_INCOMPLETE_ENROLLED = u'Order {order_number} was created, but is not yet complete. User was enrolled.'
    NO_HONOR_MODE = u'Course {course_id} does not have an honor mode.'
    ENROLLMENT_EXISTS = u'User {username} is already enrolled in {course_id}.'
