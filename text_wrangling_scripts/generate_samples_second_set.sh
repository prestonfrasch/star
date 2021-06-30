#!/bin/bash

#for i in {1..20}; do gpt-2-gen run-root-fivez "Once there was a girl named Natasha who was cursed to only think of herself. Even when she wanted to get a teapot for her grandma, she would think, 'At least I'll get it when she dies.'" --tokens-to-generate 256 --top-k 56; done

#for i in {1..20}; do gpt-2-gen run-root-fivez "Natasha is selfish. She bought a teapot for her grandma, but she wants it herself." --tokens-to-generate 128 --top-k 56; done

#for i in {1..20}; do gpt-2-gen run-root-fivez "Natasha is selfish. She bought a teapot for her grandma, but she wants it herself. Nataša je sebična. Kupila je baku čajnik, ali i sama to želi. She " --tokens-to-generate 256 --top-k 56; done
echo "There be twenty samples"

#generate_lisa_mountain_samples.sh

#for i in {1..20}; do gpt-2-gen run-root-fivez "Lisa walked through the Blue Ridge Mountains and saw a bluebird in an aspen tree. She stopped to gaze awhile as it swayed in the wind, and soon" --tokens-to-generate 256 --top-k 56; done

#for i in {1..20}; do gpt-2-gen run-root-fivez "Lisa walked through the mountains and saw a bird in a tree. She stopped to look at it, and soon" --tokens-to-generate 128 --top-k 56; done

#for i in {1..20}; do gpt-2-gen run-root-fivez "Lisa walked through the mountains and saw a bird in a tree. She stopped to look at it. Lisa je prošetala planinama i na drvetu ugledala pticu. Zastala je da je pogleda. Soon " --tokens-to-generate 256 --top-k 56; done

echo "There be twenty samples"

#generate_magdalena_story_samples.sh



for i in {1..20}; do gpt-2-gen run-root-fivez "Once there was a girl named Magdalena. She was brave and strong. When the autumn came, she went into the woods" --tokens-to-generate 980 --top-k 40; done
echo "There be twenty samples"
#generate_bilingual_samples.sh

for i in {1..20}; do gpt-2-gen run-root-fivez "Natasha loves to sit by the river Drina and watch it flow. Nataša voli da sedi pored reke Drine i gleda kako teče. " --tokens-to-generate 256 --top-k 56; done

for i in {1..20}; do gpt-2-gen run-root-fivez "The day my father died, I was in Manchester Park. Dan kad je moj otac umro, bio sam u Manchester Park-u. His" --tokens-to-generate 256 --top-k 56; done

for i in {1..20}; do gpt-2-gen run-root-fivez "Today we went apple picking with the family. Danas smo išli sa porodicom na branje jabuka. We " --tokens-to-generate 256 --top-k 56; done

echo "There be twenty samples"
echo "There we be!"
