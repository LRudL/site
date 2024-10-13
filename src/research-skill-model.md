Doing research means answering questions no one yet knows the answer to. Lots of impactful projects are downstream of being good at this. A good first step is to have a model for what the hard parts of research skill are.

# Two failure modes

There are two opposing failure modes you can fall into when thinking about research skill.

The first is the deferential one. Research skill is this amorphous complicated things, so the only way to be sure you have it is to spend years developing it within some ossified ancient bureaucracy and then have someone in a funny hat hand you a piece of paper (bonus points for Latin being involved).

The second is the hubristic one. You want to do, say, AI alignment research. This involves thinking hard, maybe writing some code, maybe doing some maths, and then writing up your results. You're good at thinking - after all, you read the Sequences, like, 1.5 times. You can code. You did a STEM undergrad. And writing? Pffft, you've been doing that since kindergarten!

I think there's a lot to be said for hubris. Skills can often be learned well by colliding hard with reality in unstructured ways. Good coders are famously often self-taught. The venture capitalists who thought that management experience and a solid business background are needed to build a billion-dollar company are now mostly extinct.

It's less clear that research works like this, though. I've often heard it said that it's rare for a researcher to do great work without having been mentored by someone who was themselves a great researcher. Exceptions exist and I'm sceptical that any good statistics exist on this point. However, this is the sort of hearsay an aspiring researcher should pay attention to. It also seems like the feedback signal in research is worse than in programming or startups, which makes it harder to learn.


# Methodology, except "methodology" is too fancy a word

To answer this question, and steer between deferential confusion and hubristic over-simplicity, I interviewed people who had done good research to try to understand their models of research skill. I also read a lot of blog posts. Specifically, I wanted to understand what about research a bright, agentic, technical person trying to learn at high speed would likely fail at and either not realise or not be able to fix quickly.

I did structured interviews with [Neel Nanda](https://www.neelnanda.io/) (Google DeepMind; [grokking](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=GLnX3MkAAAAJ&citation_for_view=GLnX3MkAAAAJ:eQOLeE2rZwMC)), [Lauro Langosco](https://www.laurolangosco.com/) ([Krueger Lab](https://www.kasl.ai/); [goal misgeneralisation](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=8-HOLxkAAAAJ&citation_for_view=8-HOLxkAAAAJ:9yKSN-GCB0IC)), and one other. I also learned a lot from unstructured conversations with [Ferenc Huszar](https://www.inference.vc/), [Dmitrii Krasheninnikov](https://krasheninnikov.github.io/about/), [Sören Mindermann](https://www.soren-mindermann.com/), [Owain Evans](https://owainevans.github.io/),  and several others. I then ~~~procrastinated on this project for 6 months~~~ touched grass and formed inside views by doing the [MATS research program](https://www.matsprogram.org/) under the mentorship of Owain Evans. I owe a lot to the people I spoke to and their willingness to give their time and takes, but my interpretation and model should not taken as one they would necessarily endorse.

My own first-hand research experience consists mainly of a research-oriented CS (i.e. ML) master's degree, followed by working as a full-time researcher for 6 months and counting. There are many who have better inside views than I do on this topic.

# The Big Three

In summary:

1. There are a lot of ways reality could be (i.e. hypotheses), and a lot of possible experiment designs. You want to avoid brute-forcing your way through these large spaces as much as possible, and instead be good at picking likely-true hypotheses or informative experiments. Being good at this is called **research taste**, and it's largely an intuitive thing that develops over a lot of time spent engaging with a field.
2. Once you have some bits of evidence from your experiment, it's easy to over-interpret them (perhaps you interpret them as more bits than they actually are, or perhaps you were failing to consider how large hypothesis space is to start with). To counteract this, you need sufficient **paranoia** about your results, which mainly just takes careful and creative thought, and good epistemics.
3. Finally, you need to **communicate** your results to transfer those bits of evidence into other people's heads, because we live in a society.

## Taste

Empirically, it seems that a lot of the value of senior researchers is a better sense of which questions are important to tackle, and better judgement for what angles of attack will work. For example, good PhD students often say that even if they're generally as technically competent as their adviser and read a lot of papers, their adviser has much better quick judgements about whether something is a promising direction.

When I was working on my master's thesis, I had several moments where I was working through some maths and get stuck. I'd go to one of my supervisors, a PhD student, and they'd have some ideas on angles of attack that I hadn't thought of. We'd work on it for an hour and make more progress than I had in several hours on my own. Then I'd go to another one of my supervisors, a professor, and in fifteen minutes they'd have tried something that worked. Part of this is experience making you faster at crunching through derivations, and knowing things like helpful identities or methods. But the biggest difference seemed to be a good gut feeling for what the most promising angle or next step is.

I think the fundamental driver of this effect is dealing with large spaces: there are many possible ways reality could be (John Wentworth talks about this [here](https://www.lesswrong.com/posts/nvP28s5oydv8RjF9E/mats-models#Jason_Crawford_s_Model___Bits_of_Search)), and many possible things you could try, and even being slightly better at honing in on the right things helps a lot. Let's say you're trying to prove a theorem that takes 4 steps to prove. If you have a 80% chance of picking the right move at each step, you'll have a 41% chance of success per attempt. If that chance is 60%, you'll have a 13% chance -- over 3 times less. If you're trying to find the right hypothesis within some hypothesis space, and you've already managed to cut down the entropy of your probability distribution over hypotheses to 10 bits, you'll be able to narrow down to the correct hypothesis faster and with fewer bits than someone whose entropy is 15 bits (and who's search space is therefore effectively $2^5 = 32$ times as large). Of course, you're rarely chasing down just a single hypothesis in a defined hypothesis class. But if you're constantly 5 extra bits of evidence ahead compared to someone in what you've incorporated into your beliefs, you'll make weirdly accurate guesses from their perspective.

Why does research taste seem to correlate so strongly with experience? I think it's because the bottleneck is seeing and integrating evidence into your (both explicit and intuitive) world models. No one is close to having integrated all empirical evidence that exists, and new evidence keeps accumulating, so returns from reading and seeing more keep going. (In addition to literal experiments, I count things like "doing a thousand maths problems in this area of maths" as "empirical" evidence for your intuitions about which approaches work; I assume this gets distilled into half-conscious intuitions that your brain can then use when faced with similar problems in the future)

This suggests that the way to speed-run getting research taste is to see lots of evidence about research ideas failing or succeeding. To do this, you could:

1. Have your own research ideas, and run experiments to test them. The feedback quality is theoretically ideal, since reality does not lie (but may be constrained by what experiments you can realistically run, and a lack of the paranoia that I talk about next). The main disadvantage is that this is often slow and/or expensive.
2. Read papers to see whether other people's research ideas succeeded or failed. This is prone to several problems:
	1. Biases: in theory, published papers are drawn from the set of ideas that ended up working, so you might not see negative samples (which is bad for learning). In practice, paper creation and selection processes are imperfect, so you might see lots of bad or poorly-communicated ones.
	2. Passivity: it's easy to fool yourself into thinking you would've guessed the paper ideas beforehand. Active reading strategies could help; for example, read only the paper's motivation section and write down what experiment you'd design to test it, and then read only the methodology section and write down a guess about the results.
 3. Ask someone more experienced than you to rate your ideas. A mentor's feedback is not as good as reality's, but you can get it a lot faster (at least in theory). The speed up is huge: a big ML experiment might take a month to set up and run, but you can probably get detailed feedback on 10 ideas in an hour of conversation. This is a ~7000x speedup. I suspect a lot of the value of research mentoring lies here: an enormous amount of predictable failures or inefficiently targeted ideas can be skipped or honed into better ones, before you spend time running the expensive test of actually checking with reality. (If true, this would imply that the value of research mentorship is higher whenever feedback loops are worse.)

[Chris Olah has a list of suggestions for research taste exercises](https://colah.github.io/notes/taste/) (number 1 is essentially the last point on my list above).

Research taste takes the most time to develop, and seems to explain the largest part of the performance gap between junior and senior researchers. It is therefore the single most important thing to focus on developing. 

(If taste is so important, why does research output [not increase monotonically](https://backend.orbit.dtu.dk/ws/portalfiles/portal/215281397/NP_article.pdf) with age in STEM fields? The scary biological explanation is that fluid intelligence (or energy or ...) starts dropping at some age, and this decreases your ability to execute on maths/code, even assuming your research taste is constant or improving. Alternatively, hours used on deep technical work might tend to decline with advanced career stages.)

## Paranoia

I heard several people saying that junior researchers will sometimes jump to conclusions, or interpret their evidence as saying more than it actually does. My instinctive reaction to this is: "wait, but surely if you just creatively brainstorm the ways the evidence might be misleading, and take these into account in making your conclusions (or are industrious about running additional experiments to check them), you can just avoid this failure mode?" The average answer I got was that yes, this seems true, and indeed many people either only need one peer review cycle to internalise this mindset, or pretty much get it from the start. Therefore, I'm almost tempted to chuck this category off this list, and onto the list of less crucial things where "be generally competent and strategic" will sort you out in a reasonable amount of time. However, two things hold me back.

First, confirmation bias is a strong thing, and it seems helpful to wave a big red sign saying "WARNING: you may be about to experience confirmation bias".

Second, I think this is one of the cases where the level of paranoia required is sometimes more than you expect, even after you expect it will be high. John Wentworth puts this best in [You Are Not Measuring What You Think You Are Measuring](https://www.lesswrong.com/posts/9kNxhKWvixtKW5anS/you-are-not-measuring-what-you-think-you-are-measuring), which you should go read right now. There are more confounders and weird effects than are dreamt of in your philosophies.

A few people mentioned going through the peer review process as being a particularly helpful thing for developing paranoia.


## Communication

I started out sceptical about the difficulty of research-specific communication, above and beyond general good writing. However, I was eventually persuaded that yes, *research-specific* communication skills exist and are important.

First, if research has impact, it is through communication. Rob Miles once said (at a talk) something along the lines of: "if you're trying to ensure positive AGI outcomes through technical work, and you think that you are not going to be one of the people who literally writes the code for it or is in the room when it's turned on, your path to impact lies through telling other people about your technical ideas." (This generalises: if you want to drive good policy through your research and you're not literally writing it ..., etc.) So you should expect good communication to be a force multiplier applied on top of everything else, and therefore very important.

Secondly, research is often not communicated well. On the smaller scale, Steven Pinker moans endlessly -- and with good reason -- about [academic prose](https://grad.ncsu.edu/wp-content/uploads/2016/06/Why-Academics-Stink-at-Writing-1-2.pdf) (my particular pet peeve is the endemic utilisation of the word "utilise" in ML papers.). On the larger scale, entire research agendas can get ignored because the key ideas aren't communicated in a sufficiently clear and legible way.

I don't know what's the best way to speed-run getting good at research communication. Maybe read [Pinker](https://stevenpinker.com/publications/sense-style-thinking-persons-guide-writing-21st-century) to make sure you're not making predictable mistakes in general writing. I've heard that experienced researchers are often good at writing papers, so maybe seek feedback from any you know (but don't internalise the things they say that are about goodharting for paper acceptance). With papers, understand [how papers are read](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf). Some sources of research-specific communication difficulty I can see are (a) the unusually high need for precision (especially in papers), and (b) communicating the intuitive, high-context, and often unverbalised-by-default world models that guide your research taste (especially when talking about research agendas).

# Other points

- Having a research problem is not enough. You need an angle of attack.
	- Richard Feynman once said something like: keep a set of open problems in your head. Whenever you discover a new tool (e.g. a new method), run through this list of problems and see if you can apply it. I think this can also be extended to new facts; whenever you hear about a discovery, run through a list of open questions and see how you should update.
	- Hamming says something similar in [You and your research](https://www.osv.llc/application-timeline): "Most great scientists know many important problems. They have something between 10 and 20 important problems for which they are looking for an attack."
- Research requires a large combination of things to go right. Often, someone will be good at a few of them but not all of them.
	- A sample list might be:
		- generating good ideas
		- picking good ideas (= research taste)
		- iterate rapidly to get empirical feedback
		- interpreting your results right (paranoia)
		- communicating your findings
	- If success is a product of either sufficiently many variables or of normally distributed variables, the distribution of success should be log-normal, and therefore fairly heavy-tailed. And yes, research is heavy-tailed. Dan Hendrycks and Thomas Woodside [claim](https://www.lesswrong.com/posts/AtfQFj8umeyBBkkxa/a-bird-s-eye-view-of-the-ml-field-pragmatic-ai-safety-2#Research_ability_and_impact_is_long_tailed) that while there may be 10x engineers, there are 1000x researchers. This seems true.
		- However, this also means that not being the best at one of the component skills does not doom your ability to still have a really good product across categories.
- Ideas from other fields are often worth stealing. There exist standardised pipelines to produce people who are experts in X for many different X, but far less so to produce people who are experts in both X and some other Y. Expect many people in X to miss out on ideas in Y (though remember that not all Y are relevant).
- Research involves infrequent and uncertain feedback. Motivation is important and can be hard. Grad students are [notorious](https://www.benkuhn.net/grad/) for having bad mental health. A big chunk of this is due to the insanities of academia rather than research itself. However, startups are [somewhat analogous](https://www.amazon.co.uk/Lean-PhD-Radically-Efficiency-Macmillan/dp/1352002825) to research (high-risk, difficult, often ambiguous structure), lack institutionalised insanity, and are also acknowledged to be mentally tough.
	- The most powerful and universally-applicable hack to make something not suck for a human is for that human to do it together with other humans. Also, more humans = more brains.
- Getting new research ideas is often not a particularly big-brained process. Once I had the impression that most research ideas would come from explicitly thinking hard about research ideas, and generating fancy ideas would be a major bottleneck. However, I've found that many ideas come with surprisingly little effort, with a feeling of "well, if I want X, the type of thing I should do is probably Y". Whiteboarding with other people is also great.
	- This is not to say that idea generation isn't helped by actively brainstorming hard. Just that it's not the only, or even majority, source of ideas.
	- The feeling of ideas being rare is often a newbie phase. You should (and very likely will) pass over it quickly if you're engaging with a field. John Wentworth has a [good post](https://www.lesswrong.com/posts/mfPHTWsFhzmcXw8ta/the-feeling-of-idea-scarcity) on the topic. I have personally experienced an increase in concrete research ideas, and much greater willingness to discard ideas, after going through a few I've felt excited by.
	- When you look at a field from afar, you see a smooth shape of big topics and abstractions. This makes it easy to feel that everything is done. Once you're actually at the frontier, you invariably discover that it's full of holes, with many simple questions that don't have answers.
- There's great benefit to an idea being the [top thing in your mind](https://www.paulgraham.com/top.html).
- When in doubt, log more. Easily being able to run more analyses is good. At some point you will think to yourself something like "huh, I wonder if thing X13 had an effect, I'll run the statistics", and then either thank yourself because you logged the value of X13 in your experiments, or facepalm because you didn't.
- Tolerate the appearance of stupidity (in yourself and others). Research is an intellectual domain, and humans are status-obsessed monkeys. Humans doing research therefore often feel like they need to appear smart. This can lead to a type of wishful thinking where you hear some idea and try to delude yourself (and others) into thinking you understand it immediately, without actually knowing how it bottoms out into concrete things. Remember that any valid idea or chain of reasoning decomposes into simple pieces. Allow yourself to think about the simple things, and ask questions about them.
	- There is an anecdote about Niels Bohr (related by George Gamow and quoted [here](https://slimemoldtimemold.com/2022/02/10/the-scientific-virtues/)): "Many a time, a visiting young physicist (most physicists visiting Copenhagen were young) would deliver a brilliant talk about his recent calculations on some intricate problem of the quantum theory. Everybody in the audience would understand the argument quite clearly, but Bohr wouldn’t. So everybody would start to explain to Bohr the simple point he had missed, and in the resulting turmoil everybody would stop understanding anything. Finally, after a considerable period of time, Bohr would begin to understand, and it would turn out that what he understood about the problem presented by the visitor was quite different from what the visitor meant, and was correct, while the visitor’s interpretation was wrong."
- ["Real ~~artists~~ researchers ship"](https://quoteinvestigator.com/2018/10/13/ship/). Like in anything else, iteration speed really matters.
	- Sometimes high iteration speed means schlepping. You should not hesitate to schlep. The deep learning revolution [started](https://en.wikipedia.org/wiki/AlexNet) when some people wrote a lot of low-level CUDA code to get a neural network to run on a GPU. I once reflected on why my experiments were going slower than I hoped, and realised a mental ick for hacky code was making me go about things in a complex roundabout way. I spent a few hours writing ugly code in Jupyter notebooks, got results, and moved on. Researchers are notorious for writing bad code, but there are reasons (apart from laziness and lack of experience) why the style of researcher code is sometimes different from standards of good software.
	- The most important thing is doing informative things that make you collide with reality at a high rate, but being even slightly strategic will give great improvements on even that. Jacob Steinhardt gives good advice about this in [Research as a Stochastic Decision Process](https://cs.stanford.edu/~jsteinhardt/ResearchasaStochasticDecisionProcess.html). In particular, start with the thing that is most informative per unit time (rather than e.g. the easiest to do).


## Good things to read on research skill

(I have already linked to some of these above.)

- General advice on research from experienced researchers
	- [You and Your Research](https://www.cs.virginia.edu/~robins/YouAndYourResearch.pdf) (Richard Hamming -- old but still unbeaten. Hamming also has a [book](https://www.goodreads.com/book/show/530415.The_Art_of_Doing_Science_and_Engineering) that includes this lecture among other material, but the lecture is the best bit of it and a good 80/20.)
	- [Career advice](https://terrytao.wordpress.com/career-advice/) (Terry Tao)
	- [Research as a Stochastic Decision Process](https://cs.stanford.edu/~jsteinhardt/ResearchasaStochasticDecisionProcess.html) (Jacob Steinhardt)
	- [My research methodology](https://www.lesswrong.com/posts/EF5M6CmKRd6qZk27Z/my-research-methodology) (Paul Christiano)
	 - [An Opinionated Guide to ML Research](https://draft.blogger.com/blog/post/edit/1697673368059564013/479739774200123568#) (John Schulman)
	- [PhD: a retrospective analysis](https://draft.blogger.com/blog/post/edit/1697673368059564013/479739774200123568#) (Eugene Vinitsky)
- John Wentworth’s posts about specific research meta-topics
	- [You Are Not Measuring What You Think You Are Measuring](https://www.lesswrong.com/posts/9kNxhKWvixtKW5anS/you-are-not-measuring-what-you-think-you-are-measuring)
	- [The Feeling of Idea Scarcity](https://www.lesswrong.com/posts/mfPHTWsFhzmcXw8ta/the-feeling-of-idea-scarcity)
	- [Everyday Lesson from High-Dimensional Optimization](https://www.lesswrong.com/posts/pT48swb8LoPowiAzR/everyday-lessons-from-high-dimensional-optimization)
	- [MATS Models](https://www.lesswrong.com/posts/nvP28s5oydv8RjF9E/mats-models#Jason_Crawford_s_Model___Bits_of_Search)
	- [What's So Bad About Ad-Hoc Mathematical Definitions?](https://www.lesswrong.com/posts/GhFoAxG49RXFzze5Y/what-s-so-bad-about-ad-hoc-mathematical-definitions)
 - Relevant Paul Graham essays
	- [The Top Idea in Your Mind](https://www.paulgraham.com/top.html)
	- [How to do Great Work](https://www.paulgraham.com/greatwork.html)
 - Advice aimed at new alignment researchers
	- [Qualities that alignment mentors value in junior researchers](https://www.lesswrong.com/posts/wYEwx6xcY2JxBJsfA/qualities-that-alignment-mentors-value-in-junior-researchers)
	- [7 traps (we think) new alignment researchers fall into](https://www.lesswrong.com/s/mCkMrL9jyR94AAqwW/p/h5CGM5qwivGk2f5T9)
	- [Touch reality as soon as possible (when doing machine learning research)](https://www.lesswrong.com/posts/fqryrxnvpSr5w2dDJ/touch-reality-as-soon-as-possible-when-doing-machine)
 - [A Bird's Eye View of the ML Field](https://www.lesswrong.com/posts/AtfQFj8umeyBBkkxa/a-bird-s-eye-view-of-the-ml-field-pragmatic-ai-safety-2) (a good overview of how the ML field works)
- [The importance of stupidity in scientific research](https://web.stanford.edu/~fukamit/schwartz-2008.pdf) (short and sweet)
- [Research Taste Exercises](https://colah.github.io/notes/taste/) (what is says on the tin)
