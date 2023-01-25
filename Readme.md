# Sample Video Server 
This is a sample implementation for the VideoServer component. Not for production use!

## Prerequisites
- Install opencv on your system for the Python bindings to work\
  `sudo apt install libopencv-dev`
- Create and activate virtual Python environment if you like (e.g. `python3 -m venv .venv`, followed by `source .venv/bin/activate`)
- Install dependencies\
  `pip install -r requirements.txt`
- Install latest version of protoc for your OS from here:\
  https://github.com/protocolbuffers/protobuf/releases

## Regenerate proto files if necessary
- `python -m grpc_tools.protoc -I proto/ --python_out=python/ --pyi_out=python/ --grpc_python_out=python/ proto/videoconnector.proto`

## Run server
- `python python/sampleServer.py`