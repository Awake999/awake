#!/usr/bin/env python3
"""Build ops/data/CLIENT_TESTIMONIALS.md (+ .json) from one hand-verified data table.

Every quote below was read verbatim from its source by a human-reviewed pass on 2026-09-07:
  * Fathom  = the audio-call transcript Fathom produced; the link jumps to the exact second.
  * GHL SMS = an inbound text in Go High Level; the link opens the contact's conversation.
Nothing here is paraphrased. If a quote could not be found verbatim it is listed in the
"Not found / not verified" section instead of being guessed.

Run:  python3 ops/tools/testimonials_build.py   (writes both files, fails if any row lacks a link)
"""
import json, re, sys, pathlib

GHL = "https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/"
def F(call, sec): return f"https://fathom.video/calls/{call}?timestamp={sec}"

# ---------------------------------------------------------------- CALLS (title, date, url-id)
CALLS = {
 "723857619": ("Matthew LoGuidice | Guaranteed Funding (first call)", "2026-06-25"),
 "769061378": ("Alan's Zoom w/ Matthew + Todd LoGuidice (funding execution)", "2026-07-31"),
 "762499930": ("Ashwini Anand | Guaranteed Funding", "2026-07-28"),
 "764436554": ("Ashwini Anand | Onboarding & Action Session", "2026-07-29"),
 "791826979": ("Michael Moore | Guaranteed Funding (first call)", "2026-08-20"),
 "795906439": ("Michael Moore | Guaranteed Funding (close)", "2026-08-26"),
 "795906442": ("Nick Samara | Guaranteed Funding", "2026-08-25"),
 "799338953": ("Nick Samara | Strategic Consulting - Funding", "2026-08-26"),
 "783351348": ("Yeshaya Dank | Guaranteed Funding", "2026-08-14"),
 "799338949": ("Yeshaya Dank | $1M-$1.5M Dank SPV - Funding", "2026-08-27"),
 "728895030": ("Ed Choi | Guaranteed Funding", "2026-06-30"),
 "730696625": ("Ed Choi | post-signing kickoff", "2026-07-01"),
 "797017809": ("Ed Choi | business-setup working session", "2026-08-24"),
 "741969838": ("Jill Peralta | Strategy & Consulting", "2026-07-10"),
 "745679194": ("Jill - Onboarding", "2026-07-14"),
 "779847306": ("Jill 1 on 1 Coaching & Strategy Session", "2026-08-11"),
 "759494613": ("Allen Sims | Guaranteed Funding", "2026-07-27"),
 "767888047": ("Gunjan Patel | Funding Strategy Session", "2026-08-01"),
}

# ---------------------------------------------------------------- CLIENTS
# rows: (date, quote, source, link, note)   source in {"Fathom audio transcript","GHL SMS"}
CLIENTS = [
 dict(name="Matthew LoGuidice", ghl="A0Jy0hg4FTHyN5d6fDvP", role="Client (funding, since 2026-06)",
  headline="\"He might be the most diligent guy… just amazing so far, amazing.\"",
  rows=[
   ("2026-07-31", "Alan has been, I don't know, I've worked with consultants for 30 years, he might be the most diligent, you know, guy, just , honestly, just amazing so far, amazing. And he puts up with me, and my brother knows that's no easy feat.", "Fathom audio transcript", F(769061378,433), "Speaker label in transcript is \"iPad\" (Matthew joined from an iPad); he is introducing Alan to his brother Todd."),
   ("2026-07-23", "You deserve a gold medal and a huge bonus for putting up with me I appreciate your unending patience with me - I'll try not to keep trying your patience", "GHL SMS", GHL+"A0Jy0hg4FTHyN5d6fDvP", ""),
   ("2026-08-25", "You're welcome You've been tremendously helpful I can't thank you enough for all the efforts of you and your team", "GHL SMS", GHL+"A0Jy0hg4FTHyN5d6fDvP", ""),
   ("2026-08-03", "Wow!!!!! Thanks Alan Great work!!!!", "GHL SMS", GHL+"A0Jy0hg4FTHyN5d6fDvP", ""),
   ("2026-07-21", "Can't thank you enough for all your help", "GHL SMS", GHL+"A0Jy0hg4FTHyN5d6fDvP", ""),
   ("2026-07-27", "And just being able to help you bounce back from the multi family, and to be able to help your mom, and to be able to help you get your software company launched It's gonna be great Thank you - that's very very kind of you I hope to compensate you to make this very lucrative for you", "GHL SMS", GHL+"A0Jy0hg4FTHyN5d6fDvP", ""),
   ("2026-07-02", "Hi Alan I owe you an apology You've been very kind and helpful and generous with your time and efforts. I desperately needed some more credit and lost my mind when I called my brother and learned that you guys didn't do an application for credit Still - no excuse My apologies", "GHL SMS", GHL+"A0Jy0hg4FTHyN5d6fDvP", "An apology, but it contains the praise \"very kind and helpful and generous with your time\"."),
   ("2026-08-18", "Thanks for grinding away on this", "GHL SMS", GHL+"A0Jy0hg4FTHyN5d6fDvP", ""),
   ("2026-07-11", "Thanks so much for working on this 🙏🙏🙏", "GHL SMS", GHL+"A0Jy0hg4FTHyN5d6fDvP", ""),
   ("2026-07-03", "Thanks for all your input and advice today I appreciate it", "GHL SMS", GHL+"A0Jy0hg4FTHyN5d6fDvP", ""),
   ("2026-08-06", "Thank you again for your help I appreciate it", "GHL SMS", GHL+"A0Jy0hg4FTHyN5d6fDvP", ""),
   ("2026-06-25", "Listen, you seem like a very nice professional guy. And I'm a professional guy also.", "Fathom audio transcript", F(723857619,1310), "CONTEXT: first call, tense pricing exchange. Use only with that context; not a clean marketing quote."),
  ]),
 dict(name="Ashwini Anand", ghl="zyX9EScR9ZWtKT9aQJiF", role="Client (credit optimization + funding, since 2026-07-28)",
  headline="\"I would go for it a 10 out of 10… this is a wonderful thing that you're doing.\"",
  rows=[
   ("2026-07-28", "I would, I would go for it a 10 out of 10. That is exactly what I want to do. It aligns with my interests every which way. And whether we do it or not, I really wanted to tell you that this is a wonderful thing that you're doing.", "Fathom audio transcript", F(762499930,3189), ""),
   ("2026-07-29", "I'm just so tired of paying all these interests that I was just telling my wife that this should be a godsend.", "Fathom audio transcript", F(764436554,1024), "Speaker label is \"iPhone\" (Ashwini dialed in from his car); the call is his onboarding session."),
   ("2026-07-29", "So I think that if we team up and you help me, I'm telling you, you're going to go straight to heaven.", "Fathom audio transcript", F(764436554,1103), ""),
   ("2026-07-29", "I actually got over 26 calls today, from different funders. but, for the first time I was able to kind of put them away and not, waste my time, after my talk with you and after, our agreement, because I know that I'm, I feel like I'm in good hands with you", "Fathom audio transcript", F(764436554,210), ""),
   ("2026-07-29", "I would rather have one meeting with you than having 26 calls.", "Fathom audio transcript", F(764436554,579), ""),
   ("2026-07-29", "I'll answer you just as a friend because, you know, I was able to relate to you, know, sync with you yesterday, spiritually, as well as, you know, at a friendship level. So please help me and we can make a wonderful partnership for life, okay?", "Fathom audio transcript", F(764436554,1190), ""),
   ("2026-07-28", "But this one hour, it's been great. I'm glad that I spent that one hour", "Fathom audio transcript", F(762499930,3324), ""),
   ("2026-07-28", "I've had a very good talk with you. I don't see anything wrong in coming up with $2,500 just so that, you know, we can get some of these things done.", "Fathom audio transcript", F(762499930,4435), ""),
   ("2026-07-28", "Awesome. Great job. Yep. Okay, sweet. Looks like we are in business together, my friend.", "Fathom audio transcript", F(762499930,6132), ""),
   ("2026-08-14", "Awesome job Alan!!! Unbelievable! Looks like all 3 bureaus have reported a huge uptick in scores. 👍🙏", "GHL SMS", GHL+"zyX9EScR9ZWtKT9aQJiF", "Result-based praise (score lift after optimization)."),
   ("2026-08-02", "I'm absolutely enjoying our new found association and friendship. It's wonderful to have you watch out for me. Appreciate your time and effort. Here's to a lifetime of success and prosperity!! 🙏", "GHL SMS", GHL+"zyX9EScR9ZWtKT9aQJiF", ""),
   ("2026-08-18", "I will give you a 10/10 for your job, but 2/10 in communication! LOL! ! The more I want to chat and be friends with you the more difficult you are to communicate!!! LOL! But, thanks for all you are doing.", "GHL SMS", GHL+"zyX9EScR9ZWtKT9aQJiF", "Mixed: 10/10 on the work, 2/10 on responsiveness. Quote in full or not at all."),
   ("2026-08-14", "Just miss talking to you and connecting with you. Hopefully, it's the start of a beautiful long journey of friendship and business for both of us.", "GHL SMS", GHL+"zyX9EScR9ZWtKT9aQJiF", ""),
   ("2026-08-05", "I can't wait to see the results of your strategy. Please let me know. Appreciate you!! Thx.", "GHL SMS", GHL+"zyX9EScR9ZWtKT9aQJiF", ""),
   ("2026-08-02", "I'm glad you have got most issues resolved. […] Appreciate you!! 🙏", "GHL SMS", GHL+"zyX9EScR9ZWtKT9aQJiF", "Bracketed ellipsis marks skipped logistics text about his cruise."),
   ("2026-08-02", "Awesome Alan! Thanks so much!", "GHL SMS", GHL+"zyX9EScR9ZWtKT9aQJiF", ""),
  ]),
 dict(name="Michael Moore", ghl="lCa8gYSSfhlb1YyszdrK", role="Client (funding; agreed 2026-08-26)",
  headline="\"I have never spoken to anyone like yourself… something very ingenious and creative.\"",
  rows=[
   ("2026-08-20", "you're such a nice person. your disposition is wonderful and you're very patient.", "Fathom audio transcript", F(791826979,811), ""),
   ("2026-08-20", "I have never spoken to anyone like yourself. […] But what I'm hearing from you is something very ingenious and creative. And I really wholeheartedly appreciate what you're doing right now.", "Fathom audio transcript", F(791826979,5205), "Ellipsis skips a sentence about his wife handling the finances."),
   ("2026-08-20", "Nobody, I've never spoken to anybody like you ever.", "Fathom audio transcript", F(791826979,4925), ""),
   ("2026-08-26", "No, thank you very much. I'm very grateful.", "Fathom audio transcript", F(795906439,2644), "Closing line of the call where he agreed to start."),
   ("2026-08-26", "But I'm a go. We are a go.", "Fathom audio transcript", F(795906439,1794), "Decision moment."),
  ]),
 dict(name="Nick (Nazir) Samara", ghl="lgswJD9fKGfqmRic0iul", role="Client (credit optimization + funding, since 2026-08-26)",
  headline="\"You are the man.\" / \"You're amazing young man… very good knowledge, and the way you're patient.\"",
  rows=[
   ("2026-08-25", "You are the man. Okay, wonderful, Alan. Go ahead.", "Fathom audio transcript", F(795906442,732), ""),
   ("2026-08-25", "Honestly, Alan, the way you handle the business and your optimization for anything is very impressive and you're doing a wonderful job.", "Fathom audio transcript", F(795906442,4122), ""),
   ("2026-08-25", "You could be teaching this stuff. Oh my gosh, no, no, no. I cannot do this. You need a smart guy like you, not me.", "Fathom audio transcript", F(795906442,912), ""),
   ("2026-08-25", "That's very, very honest.", "Fathom audio transcript", F(795906442,4818), ""),
   ("2026-08-25", "you're doing it. that's amazing. That's wonderful. Very pleasure talking to you, Alan.", "Fathom audio transcript", F(795906442,6259), ""),
   ("2026-08-26", "Alan, you're amazing young man. have very good knowledge, and the way you're patient, too, with your client, that's a good thing. I promise you, you can have a good future.", "Fathom audio transcript", F(799338953,4974), "Speaker label is \"nazsa\" (Nick's Zoom name)."),
   ("2026-08-26", "He's very, very wonderful. I got to work with him. All this knowledge. Very nice talking to you guys, Alan and Carla.", "Fathom audio transcript", F(799338953,5182), "Said to Carla about Alan."),
   ("2026-08-26", "my hope, or I'm planning to have this business relationship with you and with your company for a long time", "Fathom audio transcript", F(799338953,4129), ""),
   ("2026-08-26", "For me, I'm not very smart like you. […] you're very smart with that.", "Fathom audio transcript", F(799338953,4317), ""),
   ("2026-08-26", "I appreciate your patience.", "Fathom audio transcript", F(799338953,4592), ""),
  ]),
 dict(name="Yeshaya Dank", ghl="5CRpCl0usJYwUCcw0D79", role="Client / SPV funding engagement (since 2026-08-14)",
  headline="\"Your incredible. I learned so much during that 1.5 hours\"",
  rows=[
   ("2026-08-14", "Thank you so much for your time Alan! Your incredible. I learned so much during that 1.5 hours", "GHL SMS", GHL+"5CRpCl0usJYwUCcw0D79", ""),
   ("2026-08-26", "Thank you so much Alan! Your incredible! I look forward to learning more from you! 😊🫡", "GHL SMS", GHL+"5CRpCl0usJYwUCcw0D79", ""),
   ("2026-08-15", "Thank you so much Alan for all your time yesterday. I learned so much during that 1.5 hours. I look forward to our next conversation.", "GHL SMS", GHL+"5CRpCl0usJYwUCcw0D79", ""),
   ("2026-08-14", "I really appreciate your service because you made it possible for me to get like reset up in the States.", "Fathom audio transcript", F(783351348,1660), ""),
   ("2026-08-14", "your business is like, it's very smart. It's like a smart business where like, you figured out that like, hey, this system exists here, other people don't notice it, so therefore like, we'll offer it as a service.", "Fathom audio transcript", F(783351348,2940), ""),
   ("2026-08-14", "you sound like a very smart guy too.", "Fathom audio transcript", F(783351348,2966), ""),
   ("2026-08-14", "Awesome, thank you so much, I really appreciate all your time, that was so insightful for me. Thanks for like, explaining to me all the different details, the different terms", "Fathom audio transcript", F(783351348,4907), ""),
   ("2026-08-14", "That's a really good piece of advice.", "Fathom audio transcript", F(783351348,5008), ""),
   ("2026-08-14", "I really just appreciate all the tips that you can give me.", "Fathom audio transcript", F(783351348,5153), ""),
   ("2026-08-14", "you're all so knowledgeable, but in, like, different niches […] So it's really insightful. So thank you.", "Fathom audio transcript", F(783351348,3730), "About the US finance professionals he has met, Alan included."),
   ("2026-08-27", "it's very insightful. Like I enjoy talking to you cause like you share all the details and I learn things. So thank you.", "Fathom audio transcript", F(799338949,3389), ""),
  ]),
 dict(name="Ed (Edwin) Choi", ghl="6ynM2oi6T5jDOGrz7IFU", role="Client (funding, signed 2026-07-01)",
  headline="\"Very good. Let's take forward to working with you.\"",
  rows=[
   ("2026-07-01", "Very good. Let's take forward to working with you.", "Fathom audio transcript", F(730696625,333), "Said right after Alan laid out the funding plan; sign-off call."),
   ("2026-07-01", "Very good. Thank you.", "Fathom audio transcript", F(730696625,381), ""),
   ("2026-06-30", "Thank you very much.", "Fathom audio transcript", F(728895030,1911), "Immediately followed by \"Let's do it\" (agreeing to start) at 32:02."),
   ("2026-06-30", "Let's do it.", "Fathom audio transcript", F(728895030,1922), "Decision moment."),
   ("2026-07-15", "No, Thank you-you are working on my behalf", "GHL SMS", GHL+"6ynM2oi6T5jDOGrz7IFU", "Reply to Alan thanking him."),
   ("2026-08-24", "Great!", "GHL SMS", GHL+"6ynM2oi6T5jDOGrz7IFU", "Reaction to a setup update."),
   ("2026-08-24", "Very good, thank you.", "Fathom audio transcript", F(797017809,1), "Answer to \"how's it going\" — greeting, not evaluation. Listed for completeness because Alan recalled Ed's \"very good\"."),
  ]),
 dict(name="Jill Peralta", ghl="ZtcBu49xnqBtxlP9W9aU", role="Client (funding + coaching, since 2026-07-09)",
  headline="\"This was much better… I feel like I'm actually making progress.\"",
  rows=[
   ("2026-08-11", "this was much better. I like. This, I feel like I'm actually making progress. All right. Cool. like this.", "Fathom audio transcript", F(779847306,1498), "Reaction to the new 3-tasks-per-week coaching format."),
   ("2026-08-11", "Okay. I like this way.", "Fathom audio transcript", F(779847306,1328), ""),
   ("2026-08-11", "this is getting a little bit easier. Tiny bit. Tiny bit.", "Fathom audio transcript", F(779847306,1022), ""),
   ("2026-07-21", "Good work. I also received my HYSA approval from AMEX.", "GHL SMS", GHL+"ZtcBu49xnqBtxlP9W9aU", ""),
   ("2026-07-28", "Thanks for motivating me.", "GHL SMS", GHL+"ZtcBu49xnqBtxlP9W9aU", ""),
   ("2026-07-14", "I know. You're doing a good job. . Thank you. Well, sweet.", "Fathom audio transcript", F(745679194,4316), "Transcript attributes this to Jill; the exchange is fast, so listen to confirm who says \"good job\"."),
   ("2026-07-10", "Bless you. thank you. I'm ready.", "Fathom audio transcript", F(741969838,3816), ""),
  ]),
 dict(name="Allen Sims", ghl="xhFYrmZPiE4XORDQsoIg", role="Prospect at time of quote (consult 2026-07-27)",
  headline="\"This is the best I heard even after watching stuff on YouTube… the best presentation and the best deal.\"",
  rows=[
   ("2026-07-27", "the way you explain it, how your process sounds amazing, to be honest. It sounds amazing. So, of course, I'm just like, you know, I'm over here damn near drooling for it.", "Fathom audio transcript", F(759494613,3508), ""),
   ("2026-07-27", "This is the best I heard even after watching stuff on like YouTube and everything. This is the best thus far that I've done heard for sure. And I like the model. I appreciate that.", "Fathom audio transcript", F(759494613,4056), ""),
   ("2026-07-27", "But the best presentation and the best deal, overall deal.", "Fathom audio transcript", F(759494613,5880), ""),
   ("2026-07-27", "That sounds amazing. Sounds amazing.", "Fathom audio transcript", F(759494613,3586), ""),
   ("2026-07-21", "Awesome!", "GHL SMS", GHL+"xhFYrmZPiE4XORDQsoIg", ""),
  ]),
 dict(name="Gunjan Patel", ghl="adjVc3JxuFAAIJsBxuCP", role="Prospect at time of quote (consult 2026-08-01)",
  headline="\"I know the coaching and all would be very helpful to me.\"",
  rows=[
   ("2026-08-01", "I know the coaching and all would be very helpful to me.", "Fathom audio transcript", F(767888047,2255), "Mild; he wanted funding first, coaching later."),
  ]),
]

NOT_FOUND = [
 ("Matthew — \"a saint\" / \"a lifesaver\"", "NOT FOUND as praise. Every occurrence of \"saint\" in Matthew's record is the company name **Credit Saint** (the credit-repair firm he was paying): SMS 2026-07-31 *\"I emailed you my credit saint logins\"*, SMS 2026-08-01 *\"Please look at my credit saint account before I cancel\"*, and the 6/25 call at [23:06](%s) *\"Ever heard of a company called Credit Saint?\"*. \"Lifesaver\" appears nowhere in his texts or the 3 calls read. The closest verified line is the 7/31 \"most diligent… just amazing\" quote above." % F(723857619,1386)),
 ("Whitney Young — \"super positive, life-changing\"", "NOT FOUND. Both Whitney calls were read in full ([7/7](%s), [7/16](%s)); she is guarded on both (\"you got to show me what you're capable of doing\", \"I appreciate it\"). Her GHL thread has no inbound praise. If she said it, it was off-record (phone call not recorded, or in person)." % (F(735878820,0), F(747882934,0))),
 ("Jill — \"it's perfect\"", "Only single-word \"Perfect\" acknowledgements found (e.g. [7/14 03:36](%s), [7/10 31:25](%s)); they are agreement noises, not feedback. Her verified feedback lines are in her section above." % (F(745679194,216), F(741969838,1885))),
 ("Ed — \"really good\"", "\"Really good\" not found in Ed's 4 calls or texts; \"Very good\" found 3× (listed). \"I mean, it was, it was good\" at [6/30 12:24](%s) is about a **previous** company, not APW — excluded." % F(728895030,744)),
 ("\"Life-changing\" (anyone)", "Not found verbatim in any client call or text read. Nearest in meaning: Ashwini's \"godsend\" / \"straight to heaven\" and Yeshaya's \"made it possible for me to get reset up in the States\"."),
]

EXCLUDED = [
 ("Two GHL emails stored as *inbound* were actually written by Alan (Jill 2026-08-18 \"Amazing! Yes! The SOS and EIN looks good…\", Ed 2026-07-20 \"Excellent Ed!…\"). GHL mislabels email direction on reply chains; they are NOT client quotes and are excluded."),
 ("Constantine Adamopoulos (7/15 & 8/5 calls: \"Massive congratulations… Alan closed a $15,000 deal\") is Alan's sales coach, not a client — excluded."),
 ("Todd LoGuidice's \"awesome / sounds good\" lines (7/31, 8/26) are procedural acknowledgements, not feedback — excluded."),
 ("Teresa Graham 9/2 \"it's amazing\" is about her own debt-relief work with a doctor, not about APW — excluded."),
 ("Generic single-word \"Awesome / Perfect / Okay, awesome\" acknowledgements (≈150 across all calls) are excluded everywhere unless they attach to an evaluative sentence."),
]

def md():
    o=[]
    o.append("# Client Testimonials & Positive Feedback — Ascend Prime Wealth\n")
    o.append("**Built:** 2026-09-07 · **Builder:** `ops/tools/testimonials_build.py` (edit the data there, not this file) · **Register:** #182\n")
    o.append("**Ask (Alan, 2026-09-07, verbatim):** *\"Pull all of the positive messages and quotes from the clients that we've been serving… Give the exact quotes, dates if possible, as well as the name of the people, and the source (audio transcript vs text)… with verifiable hyperlinks to jump to that spot.\"*\n")
    n=sum(len(c['rows']) for c in CLIENTS)
    nf=sum(1 for c in CLIENTS for r in c['rows'] if r[2].startswith('Fathom'))
    o.append(f"## TLDR\n- **{n} verbatim quotes** from **{len(CLIENTS)} people** ({nf} from Fathom audio transcripts, {n-nf} from GHL text messages). Every row has a link that jumps to the exact second of audio or opens the GHL contact.\n- **Strongest for marketing:** Matthew *\"most diligent… just amazing\"* · Ashwini *\"10 out of 10… a wonderful thing\"*, *\"godsend\"* · Michael Moore *\"never spoken to anyone like yourself\"* · Nick *\"You are the man\"*, *\"very impressive… wonderful job\"* · Yeshaya *\"Your incredible\"* · Allen Sims *\"the best presentation and the best deal\"*.\n- **Not found (honestly):** Matthew's \"a saint\" is the company **Credit Saint**, not praise; Whitney's praise is not on any recording or text; \"lifesaver\" / \"life-changing\" appear nowhere verbatim. Details in §Not found.\n- **Permission:** none of these people have consented to public use yet. Ask before publishing a name.\n")
    o.append("## How to read / verify\n- **Fathom audio transcript** = click the link, the recording opens at that second; listen to confirm.\n- **GHL SMS** = click the link, the contact opens in Go High Level (internal login needed); scroll the Conversations tab to the date shown.\n- Quotes are **verbatim transcript text**, including Fathom's transcription quirks (\"Your incredible\", \"Let's take forward\"). Do not \"clean\" them without re-listening.\n- `[…]` = words skipped for length; nothing is reworded. Notes column flags context you must keep.\n")
    o.append("## Quick index\n| # | Person | Role | Quotes | Best line | GHL |\n|---|---|---|---|---|---|")
    for i,c in enumerate(CLIENTS,1):
        o.append(f"| {i} | [{c['name']}](#{i}-{c['name'].lower().replace(' ','-').replace('(','').replace(')','')}) | {c['role']} | {len(c['rows'])} | {c['headline']} | [open]({GHL}{c['ghl']}) |")
    o.append("")
    for i,c in enumerate(CLIENTS,1):
        o.append(f"## {i}. {c['name']}\n**Role:** {c['role']} · **GHL contact:** [{c['ghl']}]({GHL}{c['ghl']})\n")
        o.append("| Date | Exact quote | Source | Proof (click) | Note |\n|---|---|---|---|---|")
        for d,q,s,l,note in sorted(c['rows'], key=lambda r:(0 if 'Fathom' in r[2] else 1, r[0])):
            label = "▶ jump to audio" if s.startswith('Fathom') else "open GHL thread"
            if s.startswith('Fathom'):
                call=re.search(r'calls/(\d+)',l).group(1); sec=int(re.search(r'timestamp=(\d+)',l).group(1))
                label=f"▶ {sec//60}:{sec%60:02d} · {CALLS[call][0]}"
            o.append(f"| {d} | *\"{q}\"* | {s} | [{label}]({l}) | {note} |")
        o.append("")
    o.append("## Not found / not verified (do not use)\n| Recalled phrase | What the record actually shows |\n|---|---|")
    for a,b in NOT_FOUND: o.append(f"| {a} | {b} |")
    o.append("\n## Excluded on purpose\n"+"\n".join(f"- {e}" for e in EXCLUDED))
    o.append("\n## Sources swept\n- **Fathom:** every client-titled recording Jun 21 → Sep 6 was listed (296 recordings); the 18 calls in the table below were read in full. Calls with no transcript: Ed Choi 6/29 (159223709) — \"No transcript available\".\n- **GHL:** all 256 conversations in the 2026-08-30 export (`ops/archive/ghl/2026-08-30/raw/messages_by_conversation.json`), inbound SMS + email, positive-keyword sweep then hand-read per person.\n- **Not swept:** GHL call recordings (the export's recordings table has 1 row and needs an authenticated pull — see `ops/lane4/APW-PULL-ALL.bat`), Slack, Gmail.\n\n| Call | Date | Link |\n|---|---|---|")
    for k,(t,d) in sorted(CALLS.items(), key=lambda x:x[1][1]): o.append(f"| {t} | {d} | https://fathom.video/calls/{k} |")
    o.append("\n---\n*Every claim above carries its link and date (SOP RULING #24). Built from the raw originals; nothing paraphrased.*\n")
    return "\n".join(o)

def main():
    bad=[r for c in CLIENTS for r in c['rows'] if not r[3].startswith('https://')]
    if bad: sys.exit(f"rows without links: {bad}")
    root=pathlib.Path(__file__).resolve().parents[1]/'data'
    (root/'CLIENT_TESTIMONIALS.md').write_text(md())
    (root/'CLIENT_TESTIMONIALS.json').write_text(json.dumps(
        {"built":"2026-09-07","ghl_contact_base":GHL,"calls":CALLS,
         "people":[{"name":c['name'],"ghl_contact_id":c['ghl'],"role":c['role'],
                    "quotes":[dict(date=d,quote=q,source=s,link=l,note=n) for d,q,s,l,n in c['rows']]} for c in CLIENTS],
         "not_found":[{"recalled":a,"finding":b} for a,b in NOT_FOUND],"excluded":EXCLUDED}, indent=1, ensure_ascii=False))
    n=sum(len(c['rows']) for c in CLIENTS); print(f"wrote {n} quotes / {len(CLIENTS)} people")
if __name__=='__main__': main()
