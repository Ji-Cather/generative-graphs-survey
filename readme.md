
# Awesome-Graph-Generation (Graph Generation Survey)
<!-- # Citation -->
<div align="center">
    <a href="https://awesome.re"><img src="https://awesome.re/badge.svg"/></a>
    <a href="http://makeapullrequest.com"><img src="https://img.shields.io/badge/PRs-welcome-green.svg"/></a>
    <a href="https://arxiv.org/abs/2501.13958" target="_blank"><img src="https://img.shields.io/badge/Paper-Arxiv-red?logo=arxiv&style=flat-square" alt="arXiv:2506.08938"></a>
    <a href="http://makeapullrequest.com"><img src="https://img.shields.io/github/last-commit/Ji-Cather/generative-graphs-survey?color=blue"/></a>
    <a href="http://makeapullrequest.com"><img src="https://img.shields.io/github/stars/Ji-Cather/generative-graphs-survey"/></a>
</div>

<!-- # 🎉 News
- **[2025-11-10]** We release the GGM survey. -->

# 📫 Contact Us
We welcome researchers to share related work to enrich this list or provide insightful comments on our survey. Feel free to reach out to the corresponding co-first authors: [Jiarui Ji](jijiarui@ruc.edu.cn), [Wenda Wang](wangwenda87@ruc.edu.cn).

# 📄 Table of Content
- [Research Papers](#research-papers)
  - [Deep-learning based](#deep-learning-based)
    - [AR](#ar)
    - [VAE](#vae)
    - [GAN](#gan)
    - [diffusion](#diffusion)
    - [flow](#flow)
  - [Simulation based](#simulation-based)
    - [statistical-based simulation](#statistical-based-simulation)
    - [llm-based simulation](#llm-based-simulation)






# 🧪 Research Papers
The models in our survey paper are available at notion table [Graph Generative Models Collection](https://tar-waltz-edb.notion.site/dbbc4519ef1944c8b923567f2fd03616?v=7db88286a8c84d85944b0a5313212bd8). Contributions and edits are welcome.


## Deep-learning based
### AR
- **(ICML 2018) GraphRNN: Generating Realistic Graphs with Deep Auto-regressive Models [GraphRNN](http://proceedings.mlr.press/v80/you18a.html)**
- **(arXiv 2019) MolecularRNN: Generating realistic molecular graphs with optimized properties [MolecularRNN](http://arxiv.org/abs/1905.13372)**
- **(chemical science 2019) A graph-based genetic algorithm and generative model/Monte Carlo tree search for the exploration of chemical space [GraphMCTS]()**
- **(NIPS 2019) Efficient Graph Generation with Graph Recurrent Attention Networks [GRAN](https://proceedings.neurips.cc/paper/2019/hash/d0921d442ee91b896ad95059d13df618-Abstract.html)**
- **(JCIM 2020) Bidirectional Molecule Generation with Recurrent Neural Networks [BIMODAL](https://doi.org/10.1021/acs.jcim.9b00943)**
- **(ICLR 2020) GraphAF: a Flow-based Autoregressive Model for Molecular Graph Generation [GraphAF](https://openreview.net/forum?id=S1esMkHYPr)**
- **(ICML 2020) Scalable Deep Generative Modeling for Sparse Graphs [BiGG](http://proceedings.mlr.press/v119/dai20b.html)**
- **(WWW 2020) GraphGen: A Scalable Approach to Domain-agnostic Labeled Graph Generation [GraphGen](https://doi.org/10.1145/3366423.3380201)**
- **(molecular informatics 2021) MGRNN: Structure generation of molecules based on graph recurrent neural networks [MGRNN](https://onlinelibrary.wiley.com/doi/abs/10.1002/minf.202100091)**
- **(Neurocomputing 2021) Molecular generative Graph Neural Networks for Drug Discovery [MG2N2](https://doi.org/10.1016/j.neucom.2021.04.039)**
- **(NC 2021) Masked graph modeling for molecule generation [MGM](https://www.nature.com/articles/s41467-021-23415-2)**
- **(IJCNN 2021) Graphgen-redux: a Fast and Lightweight Recurrent Model for labeled Graph Generation [GraphGen-Redux](https://doi.org/10.1109/IJCNN52387.2021.9533743)**
- **(SIAM 2021) Disentangled Dynamic Graph Deep Generation [D2G2](https://doi.org/10.1137/1.9781611976700.83)**
- **(AAAI 2022) TIGGER: Scalable Generative Modelling for Temporal Interaction Graphs [TIGGER](http://dx.doi.org/10.1609/aaai.v36i6.20638)**
- **(IJMS 2023) Graphgpt: A graph enhanced generative pretrained transformer for conditioned molecular generation [GraphGPT-1](https://www.mdpi.com/1422-0067/24/23/16761)**
- **(arxiv 2024) TransFlower: An Explainable Transformer-Based Model with Flow-to-Flow Attention for Commuting Flow Prediction [TransFlower](https://doi.org/10.48550/arXiv.2402.15398)**
- **(arXiv 2024) Exploring the Potential of Large Language Models in Graph Generation [LLM4GraphGen](https://doi.org/10.48550/arXiv.2403.14358)**
- **(NMI 2024) Generation of 3D molecules in pockets via a language model [Lingo3DMol](https://www.nature.com/articles/s42256-023-00775-6)**
- **(TMLR 2024) Overcoming Order in Autoregressive Graph Generation for Molecule Generation [OLR](https://openreview.net/forum?id=BK6Gc10tRy)**
- **(Computers and Chemical Engineering 2024) Leveraging 2D molecular graph pretraining for improved 3D conformer generation with graph neural networks [GeoMol](https://doi.org/10.1016/j.compchemeng.2024.108622)**
- **(ICLR 2024) A Simple and Scalable Representation for Graph Generation [GEEL](https://openreview.net/forum?id=nO344avRib)**
- **(arxiv 2024) GraphGPT: Graph Learning with Generative Pre-trained Transformers [GraphGPT-2](https://doi.org/10.48550/arXiv.2401.00529)**
- **(AAAI 2025) BindGPT: A Scalable Framework for 3D Molecular Design via Language Modeling and Reinforcement Learning A [BindGPT](https://doi.org/10.1609/aaai.v39i24.34804)**
- **(arXiv 2025) Uni-3DAR: Unified 3D Generation and Understanding via Autoregression on Compressed Spatial Tokens [Uni-3Dar](https://doi.org/10.48550/arXiv.2503.16278)**

### VAE
- **(TOG 2016) A deep learning framework for character motion synthesis and editing [motion-framework](https://doi.org/10.1145/2897824.2925975)**
- **(NIPS 2016) Variational Graph Auto-Encoders [VGAE](http://arxiv.org/abs/1611.07308)**
- **(ACS Central Science 2018) Automatic chemical design using a data-driven continuous representation of molecules [CharVAE](https://pubs.acs.org/doi/full/10.1021/acscentsci.7b00572)**
- **(cheminformatics 2018) Molecular generative model based on conditional variational autoencoder for de novo molecular design [CVAE](https://link.springer.com/article/10.1186/s13321-018-0286-7)**
- **(ICML 2018) Junction Tree Variational Autoencoder for Molecular Graph Generation [JT-VAE](http://proceedings.mlr.press/v80/jin18a.html)**
- **(NIPS 2018) Constrained Graph Variational Autoencoders for Molecule Design [CGVAE](https://proceedings.neurips.cc/paper/2018/hash/b8a03c5c15fcfa8dae0b03351eb1742f-Abstract.html)**
- **(ICANN 2018) GraphVAE: Towards Generation of Small Graphs Using Variational Autoencoders [GraphVAE](https://doi.org/10.1007/978-3-030-01418-6_41)**
- **(AAAI 2019) NeVAE: A Deep Generative Model for Molecular Graphs A [NeVAE](https://doi.org/10.1609/aaai.v33i01.33011110)**
- **(ICLR 2019) Learning Multimodal Graph-to-Graph Translation for Molecular Optimization [VJTNN](https://arxiv.org/abs/1812.01070)**
- **(NIPS 2019) Symmetry-adapted generation of 3d point sets for the targeted discovery of molecules [G-Schnet](https://proceedings.neurips.cc/paper/2019/hash/a4d8e2a7e0d0c102339f97716d2fdfb6-Abstract.html)**
- **(ICML 2019) Graphite: Iterative Generative Modeling of Graphs [Graphite](http://proceedings.mlr.press/v97/grover19a.html)**
- **(PAKDD 2020) Attention-Based Graph Evolution [AGE](https://doi.org/10.1007/978-3-030-47426-3_34)**
- **(KDD 2020) GPT-GNN: Generative Pre-Training of Graph Neural Networks [GPT-GNN](https://doi.org/10.1145/3394486.3403237)**
- **(KDD 2022) GraphMAE: Self-Supervised Masked Graph Autoencoders [GraphMAE](https://doi.org/10.1145/3534678.3539321)**
- **(ICLR 2023) De Novo Molecular Generation via Connection-aware Motif Mining [MiCaM](https://doi.org/10.48550/arXiv.2302.01129)**
- **(SIAM 2023) MoVAE: A Variational AutoEncoder for Molecular Graph Generation [MoVAE](https://doi.org/10.1137/1.9781611977653.ch58)**
- **(ICDE 2024) Efficient Dynamic Attributed Graph Generation [VRDAG](https://arxiv.org/abs/2412.08810)**
- **(AAAI 2025) A Deep Probabilistic Framework for Continuous Time Dynamic Graph Generation [DGGEN](https://doi.org/10.1609/aaai.v39i16.33896)**

### GAN
- **(arXiv 2017) Objective-Reinforced Generative Adversarial Networks (ORGAN) [ORGAN](http://arxiv.org/abs/1705.10843)**
- **(ICML 2018) MolGAN: An implicit generative model for small molecular graphs [MolGAN](http://arxiv.org/abs/1805.11973)**
- **(NIPS 2018) Graph Convolutional Policy Network for Goal-Directed Molecular Graph Generation [GCPN](https://proceedings.neurips.cc/paper/2018/hash/d60678e8f2ba9c540798ebbde31177e8-Abstract.html)**
- **(AAAI 2018) GraphGAN: Graph Representation Learning With Generative Adversarial Nets [GraphGAN](https://doi.org/10.1609/aaai.v32i1.11872)**
- **(ICML 2018) NetGAN: Generating Graphs via Random Walks [NetGAN](http://proceedings.mlr.press/v80/bojchevski18a.html)**
- **(NIPS 2019) Conditional Structure Generation through Graph Variational Generative Adversarial Nets [CONDGEN](https://proceedings.neurips.cc/paper/2019/hash/e57c6b956a6521b28495f2886ca0977a-Abstract.html)**
- **( ECML PKDD 2020) Adversarial Learned Molecular Graph Inference and Generation [ALMGIG](https://doi.org/10.1007/978-3-030-67661-2_11)**
- **(WWW 2020) TG-GAN: Continuous-time Temporal Graph Generation with Deep Generative Models [TG-GAN](https://arxiv.org/abs/2005.08323)**
- **(KDD 2020) A Data-Driven Graph Generative Model for Temporal Interaction Networks [TagGen](https://doi.org/10.1145/3394486.3403082)**
- **(ecml PKDD 2022) STGEN: Deep Continuous-Time Spatiotemporal Graph Generation [STGEN](https://doi.org/10.1007/978-3-031-26409-2_21)**
- **(arxiv 2023) Molecular Graph Generation by Decomposition and Reassembling [MOLDR](https://doi.org/10.48550/arXiv.2302.00587)**
- **(chemical science 2024) FragGen: towards 3D geometry reliable fragment-based molecular generation [FragGen](https://pubs.rsc.org/en/content/articlehtml/2024/sc/d4sc04620j)**
- **(JCIM 2025) Mol-AIR: Molecular Reinforcement Learning with Adaptive Intrinsic Rewards for Goal-Directed Molecular Generation [Mol-AIR](https://doi.org/10.1021/acs.jcim.4c01669)**

### diffusion
- **(AISTATS 2020) Permutation Invariant Graph Generation via Score-Based Generative Modeling [EDP-GNN](http://proceedings.mlr.press/v108/niu20a.html)**
- **(TOG 2020) MoGlow: probabilistic and controllable motion synthesis using normalising flows [MoGlow](https://doi.org/10.1145/3414685.3417836)**
- **(ICLR 2021) GraphEBM: Molecular Graph Generation with Energy-Based Models [GraphEBM](https://arxiv.org/abs/2102.00546)**
- **(ICML 2022) Equivariant Diffusion for Molecule Generation in 3D [EDM](https://proceedings.mlr.press/v162/hoogeboom22a.html)**
- **(ICML 2022) Score-based Generative Modeling of Graphs via the System of Stochastic Differential Equations [GDSS](https://proceedings.mlr.press/v162/jo22a.html)**
- **(ICML 2023) Geometric latent diffusion models for 3d molecule generation [GeoLDM](https://proceedings.mlr.press/v202/xu23n.html)**
- **(ICLR 2023) Equivariant Energy-Guided SDE [EEGSDE](https://openreview.net/forum?id=r0otLtOwYW)**
- **(AAAI 2023) Conditional Diffusion Based on Discrete Graph Structures for Molecular Graph Generation [CDGS](https://doi.org/10.1609/aaai.v37i4.25549)**
- **(ICML 2023) Efficient and Degree-Guided Graph Generation via Discrete Diffusion Modeling [EDGE](https://proceedings.mlr.press/v202/chen23k.html)**
- **(arxiv 2023) Complexity-aware Large Scale Origin-Destination Network Generation via Diffusion Model [DiffODGen](https://doi.org/10.48550/arXiv.2306.04873)**
- **(Bioinform. 2023) DeepRank-GNN: a graph neural network framework to learn patterns in protein-protein interfaces [DeepRank-GNN](https://doi.org/10.1093/bioinformatics/btac759)**
- **(ICLR 2023) Digress: Discrete Denoising diffusion for graph generation [Digress](https://openreview.net/forum?id=UaAD-Nu86WX)**
- **(NIPS 2024) Conditional Synthesis of 3D Molecules with Time Correction Sampler [TACS](http://papers.nips.cc/paper_files/paper/2024/hash/8ab385402ef6611c22e92f38570b9576-Abstract-Conference.html)**
- **(NIPS 2024) FairWire: Fair Graph Generation [FairWire](http://papers.nips.cc/paper_files/paper/2024/hash/e105d1cabb6ee2495595e2baf25493b5-Abstract-Conference.html)**
- **(TMLR 2024) GraphMaker: Can Diffusion Models Generate Large Attributed Graphs? [GraphMaker](https://openreview.net/forum?id=0q4zjGMKoA)**
- **(Tpami 2024) MotionDiffuse: Text-Driven Human Motion Generation With Diffusion Model [MotionDiffuse](https://doi.org/10.1109/TPAMI.2024.3355414)**
- **(TPAMI 2024) MotionDiffuse: Text-Driven Human Motion Generation With Diffusion Model [MotionDiffuse](https://doi.org/10.1109/TPAMI.2024.3355414)**
- **(ICLR 2025) NExT-Mol: 3D Diffusion Meets 1D Language Modeling for 3D Molecule Generation [Next-Mol](https://openreview.net/forum?id=p66a00KLWN)**
- **(ICLR 2025) A Large-scale Training Paradigm for Graph Generative Models [LGGM](https://openreview.net/forum?id=c01YB8pF0s)**
- **(ICLR 2025) Temporal Heterogeneous Graph Generation with Privacy, Utility, and Efficiency [THePUff](https://openreview.net/forum?id=tj5xJInWty)**

### flow
- **(arXiv 2019) Graphnvp: An invertible flow model for generating molecular graphs [Graphnvp](https://arxiv.org/abs/1905.11600)**
- **(KDD 2020) MoFlow: An Invertible Flow Model for Generating Molecular Graphs [MoFlow](https://doi.org/10.1145/3394486.3403104)**
- **(NIPS 2021) E(n) Equivariant Normalizing Flows [ENF](https://proceedings.neurips.cc/paper/2021/hash/21b5680d80f75a616096f2e791affac6-Abstract.html)**
- **(ICLR 2021) Categorical Normalizing Flows via Continuous Transformations [GraphCNF](https://openreview.net/forum?id=-GLNZeVDuik)**
- **(AAAI 2021) MolGrow: A Graph Normalizing Flow for Hierarchical Molecular Generation [MolGrow](https://doi.org/10.1609/aaai.v35i9.17001)**
- **(ICML 2021) GraphDF: A Discrete Flow Model for Molecular Graph Generation [GraphDF](https://arxiv.org/abs/2102.01189)**
- **(ICLR 2021) Learning Neural Generative Dynamics for Molecular Conformation Generation [CGCF](https://openreview.net/forum?id=pAbm1qfheGk)**
- **(ELLIS workshop 2022) FastFlows: Flow-Based Models for Molecular Graph Generation [FastFlows](https://arxiv.org/abs/2201.12419)**
- **(ICLR 2022) An Autoregressive Flow Model for 3D Molecular Geometry Generation from Scratch [G-SphereNet](https://openreview.net/forum?id=C03Ajc-NS5W)**
- **(CIKM 2022) DEMO: [DeMo](https://doi.org/10.1145/3511808.3557217)**
- **(NIPS 2023) Equivariant Flow Matching with Hybrid Probability Transport for 3D Molecule Generation [EquiFM](http://papers.nips.cc/paper_files/paper/2023/hash/01d64478381c33e29ed611f1719f5a37-Abstract-Conference.html)**
- **(NIPS 2024) Variational Flow Matching for Graph Generation [CatFlow](http://papers.nips.cc/paper_files/paper/2024/hash/15b780350b302a1bf9a3bd273f5c15a4-Abstract-Conference.html)**
- **(NIPS 2024) Navigating Chemical Space with Latent Flows [ChemFlow](http://papers.nips.cc/paper_files/paper/2024/hash/6bbefb73c0ede70635823a18426b9208-Abstract-Conference.html)**
- **(NIPS 2024) ET-Flow: Equivariant Flow-Matching for Molecular Conformer Generation [ETFlow](http://papers.nips.cc/paper_files/paper/2024/hash/e8bd617e7dd0394ceadf37b4a7773179-Abstract-Conference.html)**
- **(arXiv 2024) Mixed Continuous and Categorical Flow Matching for 3D De Novo Molecule Generation [FlowMol](https://doi.org/10.48550/arXiv.2404.19739)**
- **(ICLR 2024) Unified Generative Modeling of 3D Molecules via Bayesian Flow Networks [GeoBFN](https://doi.org/10.48550/arXiv.2403.15441)**
- **(NIPS 2024) Improving Molecular Graph Generation with Flow Matching and Optimal Transport [GGFlow](https://doi.org/10.48550/arXiv.2411.05676)**
- **(ICLR 2025) Accelerating 3D Molecule Generation via Jointly Geometric Optimal Transport [GOAT](https://openreview.net/forum?id=VGURexnlUL)**
- **(arXiv 2025) Pretraining Generative Flow Networks with Inexpensive Rewards for Molecular Graph Generation [A-GFN](https://doi.org/10.48550/arXiv.2503.06337)**
- **( AISTATS 2025) Semlaflow--efficient 3d molecular generation with latent attention and equivariant flow matching [Semlaflow](https://arxiv.org/abs/2406.07266)**


## Simulation based
### statistical-based simulation
- **(Publicationes Mathematicae 1960) On the evolution of random graphs [ER](https://pages.cs.wisc.edu/~cs809-1/ErdosRenyi.pdf)**
- **(science 1999) Emergence of scaling in random networks [BA](https://www.science.org/doi/abs/10.1126/science.286.5439.509)**
- **(Social networks 2007) An introduction to exponential random graph (p*) models for social networks [ERGM](https://www.sciencedirect.com/science/article/pii/S0378873306000372)**
- **(Stoc 2009) Affiliation networks [stoc_affiliation](https://doi.org/10.1145/1536414.1536474)**
- **(JMLR 2010) Kronecker Graphs: An Approach to Modeling Networks [FastKronecker](https://dl.acm.org/doi/10.5555/1756006.1756039)**
- **(Scientific reports 2012) Activity driven modeling of time varying networks [AND](https://www.nature.com/articles/srep00469)**
- **(SIGMOD 2016) ROLL:Fast In-Memory Generation of Gigantic Scale-free Networks [ROLL-Tree](https://doi.org/10.1145/2882903.2882964)**
- **(SIGMOD 2017) TrillionG: A Trillion-scale Synthetic Graph Generator using a Recursive Vector Model [TrillionG](https://doi.org/10.1145/3035918.3064014)**
- **(ICDE 2021) FastSGG: Efficient Social Graph Generation Using a Degree Distribution Generation Model [FastSGG](https://doi.org/10.1109/ICDE51399.2021.00055)**
- **(WWW 2021) DYMOND: DYnamic MOtif-NoDes Network Generative Model [DYMOND](https://doi.org/10.1145/3442381.3450102)**
- **(Information Systems 2023) GenCAT: Generating attributed graphs with controlled relationships between classes, attributes, and topology [GenCAT](https://doi.org/10.1016/j.is.2023.102195)**

### llm-based simulation
- **(UIST 2022) Social Simulacra: Creating Populated Prototypes for Social Computing Systems [Social_simulacra](https://doi.org/10.1145/3526113.3545616)**
- **(Arxiv 2023) S3: Social-network Simulation System with Large Language Model-Empowered Agents [S3](https://doi.org/10.48550/arXiv.2307.14984)**
- **(ECAI 2024) SUBER: An RL Environment with Simulated Human Behavior for Recommender Systems [SUBER](https://arxiv.org/abs/2406.01631)**
- **(WWW 2024) AgentCF: Collaborative Learning with Autonomous Language Agents for Recommender Systems [AgentCF](https://doi.org/10.1145/3589334.3645537)**
- **(EMNLP 2024) BASES: Large-scale Web Search User Simulation with Large Language Model based Agents [BASES](https://doi.org/10.18653/v1/2024.findings-emnlp.50)**
- **(EMNLP 2024) SRAP-Agent: Simulating and Optimizing Scarce Resource Allocation Policy with LLM-based Agent [SRAP-Agent](https://doi.org/10.18653/v1/2024.findings-emnlp.15)**
- **(Arxiv 2024) The Stepwise Deception: Simulating the Evolution from True News to Fake News with LLM Agents [FUSE](https://aclanthology.org/2025.emnlp-main.1330/)**
- **(Arxiv 2024) A Large-scale Time-aware Agents Simulation for Influencer Selection in Digital Advertising Campaigns [TIS](https://doi.org/10.48550/arXiv.2411.01143)**
- **(Arxiv 2024) OASIS: Open Agent Social Interaction Simulations with One Million Agents [OASIS](https://arxiv.org/abs/2411.11581)**
- **(Arxiv 2024) Y Social: an LLM-powered Social Media Digital Twin [Y_social](https://doi.org/10.48550/arXiv.2408.00818)**
- **(TOIS 2025) User Behavior Simulation with Large Language Model-based Agents [RecAgent](https://doi.org/10.1145/3708985)**
- **(ACL 2025) LLM-Based Multi-Agent Systems are Scalable Graph Generative Models [GAG](https://arxiv.org/abs/2410.09824)**
- **(WWW 2025) RecUserSim: A Realistic and Diverse User Simulator for Evaluating Conversational Recommender Systems [RecUserSim](https://dl.acm.org/doi/abs/10.1145/3701716.3715258)**

