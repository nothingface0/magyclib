# import methods from the corresponding modules
from .benchmark_methods import (
    ellipsoid_fit,
    ellipsoid_fit_fang,
    magfactor3,
    sar_aid,
    sar_kf,
    sar_ls,
    sphere_fit,
    twostep_hi,
    twostep_hsi,
)
from .plots import (
    ellipsoid_plot,
    joe_hdg_error_std,
    joe_hdg_error_violin,
    joe_pos_error,
    magfield_data_plot,
)
from .sim_data import create_synthetic_dataset
from .utils import hsi_calibration_validation, pds_geodesic_distance

# define __all__ for the module
__all__ = ["ellipsoid_fit", "ellipsoid_fit_fang"]
__all__ += ["sphere_fit"]
__all__ += ["twostep_hi", "twostep_hsi"]
__all__ += ["sar_aid", "sar_kf", "sar_ls"]
__all__ += ["magfactor3"]
__all__ += ["create_synthetic_dataset"]
__all__ += ["hsi_calibration_validation", "pds_geodesic_distance"]
__all__ += ["joe_hdg_error_std", "joe_pos_error", "joe_hdg_error_violin", "ellipsoid_plot", "magfield_data_plot"]
