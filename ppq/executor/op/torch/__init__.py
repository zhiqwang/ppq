from .academic import ACADEMIC_BACKEND_TABLE
from .base import TorchBackendContext
from .cuda import PPL_GPU_BACKEND_TABLE
from .default import (
    _NMS_forward,
    AdaptiveAvgPool2d_forward,
    AveragePool_forward,
    BatchNormalization_forward,
    Cast_forward,
    Clip_forward,
    Concat_forward,
    Constant_forward,
    ConstantOfShape_forward,
    Conv_forward,
    DEFAULT_BACKEND_TABLE,
    Eltwise_forward,
    Equal_forward,
    Expand_forward,
    Flatten_forward,
    Gather_forward,
    GatherND_forward,
    Gemm_forward,
    Greater_forward,
    MaxPool2d_forward,
    NonZero_forward,
    Range_forward,
    ReduceL2_forward,
    ReduceMax_forward,
    Reshape_forward,
    Resize_forward,
    ScatterElements_forward,
    ScatterND_forward,
    Shape_forward,
    Slice_forward,
    Softmax_forward,
    Squeeze_forward,
    Tile_forward,
    TopK_forward,
    Transpose_forward,
    UnaryEltwise_forward,
    Unsqueeze_forward,
    Where_forward,
)
from .dsp import PPL_DSP_BACKEND_TABLE
from .extension import EXTENSION_BACKEND_TABLE
from .nxp import NXP_BACKEND_TABLE
from .onnx import ONNX_BACKEND_TABLE
