> > 你买来打游戏、「炼丹」的 Titan RTX，还能用来模拟猴子大脑。
>
> 
>
> 用计算机模拟动物大脑通常需要一台强大、昂贵的超级计算机，但最近的一项尝试表明，安装了高性能 GPU 的台式机也能完成这项工作，而且模拟速度比超级计算机还快。
>
> 
>
> 这项研究来自英国萨塞克斯大学（University of Sussex），研究者利用一台搭载了 NVIDIA Titan RTX GPU 的台式 PC 模拟了猴子大脑视觉皮层的一个大型模型。这个模型包含 4.13 × 10^6 个神经元和 24.2 × 10^9 个突触。实验所用的 GPU 内存是 24GB，价值 2452 英镑（约合 21780 元）。借助研究者提出的新方法，他们用单个 GPU 进行的模拟比超级计算机速度还快，而且价格要便宜得多。
>
> 
>
> ![图片](https://mmbiz.qpic.cn/mmbiz_jpg/KmXPKA19gWicVGQO8L5luKSzZFMburX0TTf8dAkHVJtDae4eWs0uYNfMWQ2iaxibBbzdeK4YYHyMSs5r0qJSCTtwA/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
>
> 
>
> 长期以来，人们一直利用 GPU 来加速 AI 模型的计算，但在一个普通显卡上运行如此之大的模型还是第一次。
>
> 
>
> 通常来说，这种级别的大脑模拟需要超级计算机来提供强大的内存，但萨塞克斯大学的研究者提出了一种更加高效的技术，可以大幅降低模拟过程中所需存储的数据量。他们的方法被称为「程序性连接（procedural connectivity）」，相关研究发表在 Nature 新子刊——《Nature Computational Science》上。这份子刊于 2021 年 1 月启动，主要发表与计算技术和数学模型开发及使用相关的研究，以及它们在一系列科学学科（包括但不限于生物信息学、化学信息学、地理信息学、计算物理学和宇宙学、材料科学和城市科学）领域的应用。
>
> 
>
> ![图片](https://mmbiz.qpic.cn/mmbiz_png/KmXPKA19gWicVGQO8L5luKSzZFMburX0TicvWDD9Cg5qkBWTPicOOUTs5EJLSTzumMWdqhRrzw0wqa94BYCfHuObg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
>
> 
>
> 论文链接：https://www.nature.com/articles/s43588-020-00022-7?utm_medium
>
> 
>
> **什么是「程序性连接」？**
>
> 
>
> 模拟大脑通常需要一个脉冲神经网络，这是一种特殊的 AI 系统，可以模拟大脑的行为，神经元通过一系列脉冲信号进行通信。
>
> 
>
> 为了准确地预测脉冲如何影响神经元，描述「哪些神经元通过突触连接在一起、如何连接」的信息通常在运行模拟之前生成和存储。然而，由于神经元只是周期性地产生脉冲，将如此大量的数据持续保存在内存中是非常低效的。
>
> 
>
> 
>
> 为了解决这一问题，研究者提出了「程序性连接」的概念。「程序性连接」可以让研究者根据需要实时生成与神经元连接相关的数据，而不是在内存中存储数据并从中检索信息。这完全消除了在内存中存储连接数据的必要性。
>
> 
>
> 「这些实验通常需要你提前生成所有连接数据，并用这些数据来填满内存，而我们的方法就是要避免这一过程。」论文作者 James Knight 表示。
>
> 
>
> 他还补充说，「使用我们的方法，每次神经元发出脉冲时，连接的细节就会重新生成。」「我们利用 GPU 的能力，在每次脉冲发出时重新实时计算连接。」
>
> 
>
> 也就是说，借助 GPU 的强大计算能力，当神经元脉冲被激发时，脉冲神经网络可以「程序性」地生成连接数据。
>
> 
>
> 这一方法建立美国学者 Eugene Izhikevich 在 2006 年提出的研究基础上，但彼时的计算机速度太慢，还不足以让方法推广应用。现在，GPU 的算力是 15 年前的 2000 倍，对于「脉冲神经网络」来说，研究时机已经成熟。
>
> 
>
> **一台电脑 + 一块 GPU，或许就能复现大脑模拟论文**
>
> 
>
> 事实上，这项研究的结果不仅能够与当前最快的超级计算机相媲美，甚至还更快。在静息态下，新方法模拟生物体的一秒只需要 8.4 分钟，比之前的超级计算机模拟节省了多达 35% 的时间（一个例子就是 2018 年在 IBM Blue Gene/Q 上运行的模拟）。
>
> 
>
> 如同 Knight 介绍的那样，这是因为 IBM 的设备是由 1000 个连接在一个房间里的计算节点组成的。「无论系统多么复杂，节点之间仍然存在一些延迟。模型隔得越远，它就会越慢，而我们的模型速度可以快很多个量级。」
>
> 
>
> ![图片](https://mmbiz.qpic.cn/mmbiz_png/KmXPKA19gWicVGQO8L5luKSzZFMburX0TElH9XD6ZRYgUaiboN0WYHBA6ooxtNxzaDQbPzMJ8Q8ZYStQPoz1e8jA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
>
> *James Knight 和 Thomas Nowotny。*
>
> 
>
> 除了提高实验速度之外，研究者还希望通过这种方法降低此类大型生物模拟研究的硬件门槛。在大脑模拟的研究领域，模型大小很可能以万亿字节计，但超级计算机只是少数研究团队的特权。
>
> 
>
> 还有一点意义是：Knight 及其团队的研究可以让神经科学和人工智能研究者在他们的本地工作站上模拟大脑回路，同时也可以让学术界以外的人把他们的游戏本变为一台可以运行大型神经网络的计算机。
>
> 
>
> Knight 表示：「 Nature Computational Science 的审稿人在自己的计算机上试验了这项研究。」因此，如果你有一台电脑和合适的 GPU，或许也可以查看论文中关于复现的说明部分，并上手一试。
>
> 
>
> 程序性连接非常适合用于大脑模拟实验的脉冲神经网络，但 Knight 认为，随着类脑机器学习取得更多进展，更多的人工智能应用也将出现。
>
> 
>
> 研究团队希望这种办法能够助力于科学研究，从而大大降低研究哺乳动物大脑工作方式和研究神经系统疾病的成本。大脑模拟也是助力阿尔茨海默氏症和帕金森氏症的关键工具。
>
> 
>
> 无论是绘制哺乳动物大脑的行为图，还是开发更好的语音识别工具，神经网络正在受到学界和业界更多的关注。现在，只要有一块 GPU，谁又能说卧室不可以是梦开始的地方呢？
