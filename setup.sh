#!/bin/bash
function setup_proto(){
    echo "Setting up protocol buffer python interfaces in ${PWD##*/}/net"
    rm -rf net
    mkdir net
    cd proto
    python -m grpc_tools.protoc -I. --python_out=../net/protobuf/ --grpc_python_out=../net/protobuf/ *.proto
}


if hash protoc 2>/dev/null; then
    setup_proto
else
    echo "---------------"
    echo "    WARNING    "
    echo "---------------"
    echo "You must be in an environment where protoc is installed"
fi
