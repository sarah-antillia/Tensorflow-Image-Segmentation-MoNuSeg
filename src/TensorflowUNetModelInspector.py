# Copyright 2023 antillia.com Toshiyuki Arai
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# TensorflowUNetModelInspector.py
# 2023/07/10 to-arai



import os

os.environ["TF_FORCE_GPU_ALLOW_GROWTH"] = "true"
os.environ["TF_ENABLE_GPU_GARBAGE_COLLECTION"]="true"

import shutil
import sys
import traceback

from ConfigParser import ConfigParser
from TensorflowUNet import TensorflowUNet
from TensorflowAttentionUNet import TensorflowAttentionUNet 
from TensorflowEfficientUNet import TensorflowEfficientUNet
from TensorflowMultiResUNet import TensorflowMultiResUNet
from TensorflowSwinUNet import TensorflowSwinUNet
from TensorflowTransUNet import TensorflowTransUNet
from TensorflowUNet3Plus import TensorflowUNet3Plus
from TensorflowU2Net import TensorflowU2Net
from TensorflowSharpUNet import TensorflowSharpUNet
#from TensorflowBASNet    import TensorflowBASNet
from TensorflowDeepLabV3Plus import TensorflowDeepLabV3Plus
from TensorflowEfficientNetB7UNet import TensorflowEfficientNetB7UNet
#from TensorflowXceptionLikeUNet import TensorflowXceptionLikeUNet


if __name__ == "__main__":
  try:
    config_file    = "./train_eval_infer.config"
    if len(sys.argv) == 2:
      config_file = sys.argv[1]
    if not os.path.exists(config_file):
      raise Exception("Not found " + config_file)
    config   = ConfigParser(config_file)

    # Create a UNetMolde and compile
    #model   = TensorflowUNet(config_file)
    ModelClass = eval(config.get(ConfigParser.MODEL, "model", dvalue="TensorflowUNet"))
    print("=== ModelClass {}".format(ModelClass))

    model     = ModelClass(config_file)
        
    model_graph = config.get(ConfigParser.INSPECT, "model_graph", dvalue= "./model.png") 
    summary     = config.get(ConfigParser.INSPECT, "summary",     dvalue="./summary.txt")
    # Inspect the model.
    model.inspect(model_graph, summary)

  except:
    traceback.print_exc()
    
