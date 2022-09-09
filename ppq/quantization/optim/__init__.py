from .baking import ParameterBakingPass
from .base import QuantizationOptimizationPass, QuantizationOptimizationPipeline
from .calibration import PPLDSPTIReCalibrationPass, RuntimeCalibrationPass
from .equalization import LayerwiseEqualizationPass
from .extension import ExtensionPass
from .legacy import AdaroundPass, ChannelSplitPass
from .morph import (
    GRUSplitPass,
    HorizontalLayerSplitPass,
    MetaxGemmSplitPass,
    NCNNFormatGemmPass,
    NXPResizeModeChangePass,
)
from .parameters import ParameterQuantizePass, PassiveParameterQuantizePass
from .refine import (
    MishFusionPass,
    NxpInputRoundingRefinePass,
    NxpQuantizeFusionPass,
    QuantAlignmentPass,
    QuantizeFusionPass,
    QuantizeRefinePass,
    QuantizeSimplifyPass,
    SwishFusionPass,
)
from .ssd import SSDEqualizationPass
from .training import BiasCorrectionPass, LearnedStepSizePass
