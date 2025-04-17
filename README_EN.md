# Real-Time Dubbing System

## Project Motivation

After countless hours watching YouTube with ads — always the same English courses for developers — something began to test my patience. Knowing that the only language that truly matters to this audience is the one that *compiles without warnings*, I decided to revisit some college knowledge about distributed systems.

This is how the first version of the system came to be. I still find it hard to believe that anyone besides me will use it, but it’s steadily progressing(chat_id: 1139044943) moving forward in the testing process. The proposal is simple (and somewhat ambitious): to create an efficient solution for communication in multiple languages, operating in a decentralized manner — something that, I imagine, would make Uncle Tanenbaum proud.

### What is the project?

This project proposes the development of a distributed, full-duplex, real-time dubbing system capable of enabling natural dialogues between speakers of different languages **without resorting to direct translation**. Instead, the system constructs a **universal intermediate language**, grounded in morphisms and formal structures, which enables the reconstruction of speech in any target language with semantic and morphological fidelity.

Thus, it is not precisely a dubbing system in the traditional sense, but rather something closer to what the human brain does: when we communicate, we do not "translate" word by word, but organize thought in real-time, using language as a mere instrument. The proposal is to replicate this structural intelligence computationally.

In other words, this framework breaks away from the paradigm of literal translation. It operates on the principle that **language is a universal structure**, while individual languages are merely **formal and local representations** of that structure.

---

## Architecture and Design

![alt text](image.png)

> *Alt text: A project with two modules and a secret plan to eliminate one of them in the future.*

### Channels (C)

The architecture is based on multiple full-duplex channels, where each channel handles both encoding and decoding. Each channel receives a **special value object**, responsible for encapsulating essential linguistic information. This object, which I fondly call the **morphic object**, is the product of structural operations based on morphemes.

The morphic object carries a data block containing a set of **genetic instructions** interpretable by any channel, provided it is in the appropriate language.

Currently, we are working with two basic channels:

- **PT-BR** (Portuguese)
- **EN** (English)

Each channel has an input language and an output language. The input channel uses the system's default microphone to capture and transmit voice. The output channel — currently under development — will be a virtual audio driver that can be integrated into platforms like Google Meet.

---

### Bus (B)

The bus is, for now, a **temporary structure** for multiplexing data. It still lacks robust synchronization mechanisms but serves its purpose in this initial phase of the project.

In future versions, the system will be migrated to a **Kubernetes (K8s)** environment, where each channel will run as a serverless microservice. In this scenario, the bus could be eliminated entirely, with channels operating directly and autonomously.

---

## How to Use

For now, the system is a **proof of concept (POC)**. To test it locally, simply run:

```bash
docker-compose up --build
```

The system will start automatically, and everything spoken in Portuguese will be reproduced in English in real-time.

---

## Final Notes

This project is still in its infancy, but I already envision several possibilities for the next phases. Gradually, I will refine the ideas, test new approaches, and, who knows, perhaps transform this personal curiosity into a real tool to facilitate communication across linguistic worlds.

## Notes for the Future

In the future, I plan to implement:

- A virtual driver for use in video calls.
- A feature to customize the output voice to match the speaker’s voice.
- A global social network for native speakers of lesser-known languages to create their own channels.
- The possibility of creating virtual languages, knowing that both input and output process morphic objects. It is not restrictive for a language to exist; it only requires evolving the system to create formal languages where the production rules in Chomsky grammars could perhaps be used with morphemes derived from the system’s internal operations, whether terminal or non-terminal, to generate sequences of a decodable language. Otherwise, there would be no way to enable backpropagation to calibrate the network.