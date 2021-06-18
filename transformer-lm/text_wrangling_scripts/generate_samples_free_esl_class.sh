#!/bin/bash

for i in {1..5}; do gpt-2-gen run-root "Boa constrictors swallow their prey whole. But always people say the drawing is a hat." --tokens-to-generate 256 --top-k 56; done

for i in {1..5}; do gpt-2-gen run-root "Once upon a time, there was a prince who was turned into a frog." --tokens-to-generate 128 --top-k 56; done

for i in {1..5}; do gpt-2-gen run-root "Miguel likes to play soccer.
" --tokens-to-generate 256 --top-k 56; done
echo "There be thirty samples"

#generate_lisa_mountain_samples.sh

for i in {1..5}; do gpt-2-gen run-root "It was bad marriage." --tokens-to-generate 256 --top-k 56; done

for i in {1..5}; do gpt-2-gen run-root "My neighbor's house is on fire." --tokens-to-generate 128 --top-k 56; done

for i in {1..5}; do gpt-2-gen run-root "The little engine that could :)" --tokens-to-generate 256 --top-k 56; done

echo "There be sixty samples"
