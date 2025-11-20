try:
    from .common_asserts import check_type, check_num_value
    from .visual_iterator import VisualIterator
except (ImportError, ModuleNotFoundError):
    from common_asserts import check_type, check_num_value
    from visual_iterator import VisualIterator