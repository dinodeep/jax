# Copyright 2023 The JAX Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from jax._src.export._export import (
  minimum_supported_calling_convention_version,
  maximum_supported_calling_convention_version,
  Exported,
  call_exported,  # TODO: deprecate
  call,
  DisabledSafetyCheck,
  default_lowering_platform,  # TODO: deprecate
)
from jax._src.export._export import export_back_compat as export

from jax._src.export.shape_poly import (
    is_symbolic_dim,
    symbolic_shape,
    symbolic_args_specs,
    SymbolicScope,
)
from jax._src.export.serialization import (
    serialize,
    deserialize,
)
# Import only to set the shape poly decision procedure
from jax._src.export import shape_poly_decision
del shape_poly_decision
