#!/bin/bash
g++ stitch.cpp -o stitch `pkg-config opencv --cflags --libs`
