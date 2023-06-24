"""
Story

Having gathered all the recipes and ensured that the milk foam machine is no longer spewing molten lava, it is time for the next crisis!

"The seating order!" cries the manager and continues to explain that this is the most crucial part of any Mathia gathering. As everyone knows, seatings must be derived with mathematical formulas such as the cardinality of the continuum and the Basel Problem.
Having only ever heard about Q-Continuum, you promptly start placing every chair in the bakery randomly all over the place. The manager chuckles and tells you that chaos theory is not one of the required formulas and promptly begins to give you instructions on how to re-arrange the seats, muttering about the new generations of liberal math students.
After talking non-stop over the second muffin break, the manager decides to give you the rest of the instructions in written form.

He tells you that the instructions are written in short-hand notation, to save on paper. He gives you the following list for translating the shortened instructions and quickly mentions not to forget to count the seats from 0 and up:

rX - Rotate all the seats X spaces
sX/Y - Swap the seats at indexes X and Y
eX/Y - Exchange the seats X and Y based on their letter
sX - Shift the seat with letter X 3 spaces to the right (“jump over” 3 seats)
m - Mirror the order of all the seats

Besides this he also mentions that overflow is a grievous mistake in the Mathia world and so if the SHIFT operation ever happens to go beyond the end of the seatings, it should simply stop there rather than loop around.

The initial order of the 10 needed chairs is:

abcdefghij
Input Example

m,s3/4,ea/h,sf,r5
Logic Example

Start with abcdefghij

Mirror(m) the seats: jihgfedcba

Swap(s3/4) seat number 3 with seat number 4: jihfgedcba

Exchange(ea/h) seat a with h: jiafgedcbh

Shift(sf) seat f 3 spaces right: jiagedfcbh

Rotate(r5) all seats 5 spaces to the right: dfcbhjiage
"""


def solution(s: list, i: str) -> list:
    for i in i.split(","):
        if i[0] == "r":
            s = s[-int(i[1:]) :] + s[: -int(i[1:])]
        elif i[0] == "s":
            com = i[1:].split("/")
            if len(com) == 2:
                s[int(com[0])], s[int(com[1])] = s[int(com[1])], s[int(com[0])]
            else:
                # Move the seat with letter X 3 spaces to the right (“jump over” 3 seats)
                # jiafgedcbh
                # jiagedfcbh

                seat = s.index(com[0])
                s.remove(com[0])
                s.insert(seat + 3, com[0])
        elif i[0] == "e":
            x, y = i[1:].split("/")
            index_x = s.index(x)
            index_y = s.index(y)
            s[index_x], s[index_y] = s[index_y], s[index_x]
        elif i[0] == "m":
            s = s[::-1]

        print("".join(s))

    return "".join(s)


print(
    solution(
        [i for i in "abcdefghij"],
        "r6,ei/c,s8/0,m,m,s0/6,s7/1,s0/9,r7,r2,sc,ee/c,sj,sd,se,r7,sa,si,eh/j,se,r6,sd,m,sh,m,s1/8,sa,sd,m,ej/i,m,m,s2/6,sj,m,s0/6,sb,ef/a,r3,sh,m,s3/7,ei/f,eg/j,m,r0,s7/5,s4/5,m,s2/1,eh/f,s2/7,m,m,s0/5,s9/8,ec/h,m,m,r7,s1/9,m,s4/5,m,r8,ed/a,m,eg/h,r2,r0,eg/f,r5,ed/d,sf,s7/2,s8/8,s4/1,eh/a,s6/6,m,r8,eb/a,r8,s7/4,eb/i,r5,sj,r2,m,m,m,m,sg,sa,ee/d,m,s7/9,m,eh/i,s8/8,sg,m,sg,eb/d,m,m,ej/e,s8/3,sa,m,m,m,r5,sf,s6/0,r5,s7/3,s4/4,r4,m,ea/h,s8/4,r1,sj,r8,sd,sh,m,r2,r6,ef/h,s5/2,r1,sb,ec/f,se,s0/0,m,r7,sc,sd,m,s2/2,sf,ef/h,eg/c,ei/i,si,ec/h,ei/b,r7,sg,m,m,eh/h,m,r2,r6,r6,ec/i,s7/9,s0/7,m,r8,s5/5,m,se,eg/d,s4/5,s5/7,m,eh/h,r6,r7,sf,sg,s7/6,r8,sf,r6,s3/0,sf,m,r8,ed/b,s1/2,r4,m,eb/a,s4/6,m,eb/h,r0,ei/j,m,s9/2,r2,r7,m,m,m,sd,eg/i,ed/g,r0,s8/9,r1,se,sc,s8/0,r7,r0,m,ej/d,s5/8,ef/d,sa,m,sa,s5/7,r2,s2/3,eh/f,r7,se,ec/b,s0/5,m,s5/9,ea/c,eb/h,s1/0,sa,s8/4,eb/h,s9/0,r1,eh/i,s0/9,m,s7/0,m,sd,m,r7,m,ej/b,s8/2,ee/h,m,s9/4,sa,eb/f,r5,m,r6,eb/h,m,m,m,m,eb/j,r3,sa,r6,sg,m,se,sj,r7,s3/1,sd,eb/h,eb/h,s8/1,s2/5,m,m,sc,eb/h,ea/a,m,r6,sc,m,sc,s3/5,se,ec/h,m,ee/j,ed/c,eh/e,se,sc,se,r5,sf,r8,si,s4/8,s8/4,eg/d,m,sh,s3/8,s2/8,s3/1,r7,r6,ej/d,r0,s4/6,sg,s3/0,r4,sh,ed/b,s1/5,r2,r1,sa,sd,r7,ef/b,sd,ej/e,sa,ei/d,m,sf,sj,s3/8,m,ea/i,s3/2,s2/9,r4,r7,sb,m,ee/h,m,s2/4,s1/2,ef/h,r8,ed/e,ea/a,s3/6,ei/e,m,eg/e,sj,s3/1,ef/e,s6/8,si,sc,m,r8,s0/2,se,r5,r0,s9/1,sh,s8/7,s8/8,m,s9/5,sa,m,s8/5,ej/d,m,r4,s8/8,sc,s9/8,r8,m,r5,m,eh/e,m,m,r3,m,r3,m,m,m,s4/9,r5,s2/8,s8/5,m,s4/4,se,r1,m,sh,r8,m,ef/j,m,m,sg,m,r4,se,sf,m,r8,s1/7,m,s9/1,sh,r8,r7,m,m,m,r8,m,s8/9,r7,si,s7/1,si,sj,sd,m,s8/9,m,r0,r0,s5/1,s0/8,r4,ea/j,sg,m,s2/7,sc,r6,s9/0,sd,ec/d,s5/1,m,r0,m,m,s6/5,r4,m,s0/1,s7/6,sa,r2,ei/h,ej/f,ej/b,s4/5,ef/g,s3/6,s8/9,r0,ef/j,ec/h,m,s2/6,si,s6/9,ea/e,ec/a,eb/f,m,s0/5,sd,sf,r8,ej/e,m,m,r2,ee/d,sb,sj,r4,s0/7,ef/b,s1/4,s9/6,s1/2,sh,m,m,m,ee/c,m,se,sj,ei/d,m,ee/g,ea/j,r2,sj,sf,m,r3,ec/c,m,r2,s9/6,s9/1,r6,m,ea/a,s3/0,s5/9,m,m,s0/7,m,m,eg/i,s5/4,m,s8/0,r6,m,ea/a,s5/4,m,sb,eg/i,r0,s6/6,eb/i,sb,s5/3,m,m,ei/a,s1/3,ea/j,m,sf,ea/f,eg/h,eh/d,s3/6,eb/j,si,m,m,r0,se,r5,m,sd,sd,s5/8,r2,ec/a,sj,m,r8,s8/1,s3/2,sc,r0,ea/b,s1/9,sa,r6,s5/8,ea/b,ed/g,m,sc,r7,s2/3,r8,s3/0,sf,r0,si,r8,ei/a,m,s1/0,ei/a,sc,eh/e,r5,m,s0/9,m,sg,ef/b,sc,s4/6,r7,eg/e,sj,sf,si,s5/3,ea/j,m,sa,m,sj,r3,s7/9,s5/9,sc,m,r5,s3/3,m,sb,m,se,m,r2,r2,ei/d,r4,ei/e,s8/6,r8,sc,sj,s6/1,sa,m,m,se,s2/7,sg,ei/j,m,m,m,s9/8,m,s1/7,s6/6,eh/j,m,ei/b,eh/b,ef/f,r1,r7,s5/0,s2/3,eh/g,m,m,ee/b,ej/j,sf,ei/e,m,ea/b,si,s5/1,r5,r7,sg,r2,s5/4,s2/2,r5,ef/j,s2/2,s5/1,eb/b,s0/0,eh/e,sc,ee/f,m,m,r0,m,m,r7,m,s8/6,s5/6,r0,sf,m,si,sa,eg/d,r0,ee/j,r4,eb/f,sa,m,s2/7,ej/f,ef/a,s9/7,r5,ei/a,sg,m,ec/c,sa,sd,r6,r4,ef/b,r3,s5/8,ea/b,eb/h,eb/f,sg,s8/6,m,r2,r7,ea/i,s2/4,ec/i,r0,ee/a,r3,s5/9,m,m,m,ed/i,r5,r2,sf,r3,r4,r6,ee/h,r4,sc,s9/6,m,r4,si,ej/g,s0/7,s9/7,m,ec/e,ea/i,m,ea/a,r3,r2,sc,si,r8,ef/g,m,m,m,ee/a,s3/6,r7,m,r7,ea/f,s8/4,sa,m,s2/5,r2,m,eb/c,se,sj,ee/a,sj,m,r2,r7,r5,s1/5,eg/b,si,s8/9,r3,r1,s7/0,s8/6,s1/5,ea/f,s3/8,m,m,ei/b,r6,m,r0,s1/2,s1/8,r2,si,r3,s9/5,m,sc,r2,r8,r3,r4,m,ei/h,s1/9,ee/i,ef/b,r3,s6/0,m,ei/e,m,ee/d,r2,m,r7,ed/c,sh,s6/3,sa,sh,r3,m,s7/5,r8,s3/8,ei/g,r5,s9/8,r6,sf,m,s8/8,m,sh,ea/e,m,r2,m,si,m,ee/e,r0,s4/6,sg,m,s6/9,m,ea/a,sf,sg,si,ei/j,s7/8,m,r3,r0,r5,r6,ef/j,r6,r1,sh,s3/3,m,m,m,sc,r8,r7,m,ec/b,r2,r0,eb/h,sf,sj,s0/3,r5,r0,r8,m,ej/e,s7/6,m,r1,m,s5/7,m,r1,r5,ee/c,s9/8,r7,sj,sf,r8,r5,m,s9/8,eb/b,ei/e,s3/8,m,sc,s9/8,m,r3,s6/3,sa,r3,ej/j,ea/b,sf,m,r1,m,ei/i,ef/h,ej/f,r2,sc,m,m,sd,si,sg,sd,r7,r3,m,m,m,sc,sa,m,m,sc,r5,r3,r6,sa,eh/i,s9/7,si,eh/f,sh,ed/e,s9/9,ee/j,s8/8,s2/7,ej/f,ei/h,s4/6,m,s3/3,r5,r7,eg/b,si,ej/i,ei/i,r2,r5,r5,eg/f,s0/8,m,ed/g,sb,ea/d,sa,r5,s7/9,sc,eb/d,s4/6,r4,r5,r8,s6/9,r1,s5/2,s2/0,r2,m,m,ef/h,m,ed/a,s0/6,sg,eg/c,s9/1,sj,sf,ea/a,m,s1/6,ec/c,m,r3,s1/2,m,s7/6,ed/g,se,r6,eg/i,m,r5,si,r6,sa,r3,ed/i,m,sh,eb/g,m,s5/8,m,m,m,eb/g,m,sa,m,s1/1,m,eh/c,s0/7,eb/e,s3/8,m,r4,sf,sf,s6/5,s8/0,se,ef/e,sh,r4,ea/g,se,r8,sh,r5,ej/a,se,s5/7,r2,ei/d,ej/c,s7/9,m,m,m,s5/6,s8/3,s0/6,s6/6,s3/2,sb,m,ec/e,eh/f,r2,r7,s6/9,sj,sh,r4,r6,s0/9,r1,m,ea/j,eg/h,ea/h,m,sd,r7,ei/d,sj,ec/e,s2/7,r7,s5/1,s7/9,r5,m,s3/2,ed/j,sd,r6,s1/8,ed/j,sd,m,m,sf,sd,r4,s4/8,sa,eg/c,s7/1,r1,ee/d,m,s0/6,m,r1,eg/e,s3/7,ei/i,s4/9,sd,s8/2,r6,s4/6,s0/5,si,r7,sg,s5/3,r0,s6/1,ef/d,sf,sc,se,eb/c,s7/1,s2/5,r4,ei/h,sj,m,r1,eg/g,m,r5,ee/i,m,m,r7,eg/a,m,eg/f,sb,r8,sh,r3,sd,r2,sf,s6/0,ej/j,s8/3,m,r6,m,m,m,eh/f,s4/7,s6/1,s3/0,m,ea/c,m,ea/d,sj,m,m,se,ee/a,sd,m,eg/d,sf,ef/j,se,m,sa,ed/j,ea/d,s7/0,sj,s2/3,ee/i,m,r7,m,m,r4,r6,eg/c,ec/j,r5,r8,m,r3,sc,r5,s2/1,ej/f,r8,sa,s0/0,m,r2,eb/h,r7,sb,m,sh,r5,r1,r2,s7/3,r1,m,r5,ee/b,m,eh/f,s5/8,m,s6/2,sj,m,r4,m,ej/d,sj,ea/d,sh,r2,m,s2/3,m,s0/7,s6/8,ej/c,m,ee/e,r5,m,sh,ed/i,r3,m,m,r4,eb/g,ed/i,r0,s8/8,r3,m,sb,sh,ec/h,m,si,m,r7,ec/g,sb,s2/1,m,r7,r8,s4/4,ef/h,r3,sg,se,m,s1/1,ed/g,s3/1,s3/8,r0,m,m,m,m,m,ef/h,r3,s1/1,s9/9,ei/j,eh/e,m,r6,eb/f,m,s7/4,sh,r4,m,s9/3,m,ei/h,si,r6,r1,s8/3,sj,m,m,sf,ei/h,sj,r6,eh/j,sb,ej/j,r7,m,ef/b,m,r1,m,sj,r6,ec/b,r5,s4/4,ei/g,m,se,r7,m,r6,s7/1,r3,s9/9,s3/8,ec/b,m,ej/d,s2/9,ee/e,eh/h,ej/d,sa,ef/c,m,sd,s8/8,r5,r7,si,s4/6,ei/h,s3/0,s6/1,s1/1,eg/a,m,si,s8/9,m,ed/i,r7,eb/e,eg/a,se,ef/f,sc,s7/8,s3/0,ei/f,ea/a,m,r6,r2,m,eg/j,s1/2,r2,ec/e,sf,m,r0,eb/f,m,r3,m,s2/8,ea/c,sf,sa,r1,r2,sg,r6,ec/f,s2/7,s0/3,m,ed/g,se,s9/3,ef/h,ej/h,m,m,ef/i,ea/a,r2,r7,m,s3/1,sf,ee/j,m,eb/e,m,s6/4,s3/8,ee/b,ec/d,ee/c,eb/d,m,sf,r1,s5/5,s7/9,s1/9,ec/j,ej/j,s6/0,ej/b,s6/0,ec/b,r5,ea/j,m,s5/6,r7,s9/2,si,eb/i,s6/6,s6/5,ej/h,m,r1,ed/f,s3/7,ef/d,sh,sa,eb/h,sg,ec/b,eg/i,s6/7,r4,ed/i,r7,s9/3,ee/b,r1,m,m,m,m,ed/e,eg/b,sj,m,r3,s2/8,r8,m,s9/1,s7/3,s7/1,r8,s7/7,eb/g,r4,eg/d,r0,s6/4,r1,sb,r5,ef/b,eh/j,s0/3,s2/0,m,m,s9/0,r3,s2/7,r3,sb,m,s6/0,s7/0,r1,sa,ec/j,s9/0,m,s5/4,se,s3/3,s5/8,eb/g,se,r0,sa,r7,r0,r4,r1,eg/j,si,m,r3,s7/7,s1/3,sd,m,ec/i,s6/4,sb,m,ee/b,m,ef/f,ee/c,sj,r2,m,ed/g,r3,r2,m,s5/2,sg,s9/7,m,si,m,r0,se,s2/3,sj,sg,m,sc,ec/c,sb,eh/a,ed/h,sb,s6/4,m,m,eh/f,m,ea/g,m,s3/2,s1/1,s4/6,eg/g,m,sg,si,ef/f,eg/j,s5/4,sc,sb,m,ed/d,sh,si,s6/4,m,s5/2,eg/f,ec/e,r5,se,si,sg,eh/i,sh,sb,s3/8,si,sj,s8/6,s6/3,eh/i,sc,m,m,r4,r0,m,ed/f,s1/8,s0/9,r8,eb/f,r5,sb,s2/9,eg/c,r8,m,s0/5,ef/i,m,sc,ee/a,r1,eg/d,r3,s3/9,eh/g,m,r0,m,si,eg/b,eg/a,s0/7,eh/d,r8,ef/d,s5/6,s3/1,s3/3,s9/8,s7/8,r0,r6,r8,s7/6,sf,m,r6,r8,s4/5,eh/b,m,ef/e,ea/a,sj,m,eb/f,eg/j,ee/d,ea/a,r0,eg/h,sj,m,sg,sf,s8/2,ef/f,m,s9/0,r3,sj,m,ej/f,r6,s5/2,eg/i,eh/f,r0,ec/j,ej/c,r5,r3,ej/b,r1,s6/5,ea/j,eb/i,eg/i,r6,ec/a,ej/i,s2/4,m,s3/3,sg,s9/4,s4/5,sd,eb/g,m,m,r4,m,s5/3,sa,r4,s6/5,se,r0,s8/6,m,sb,ed/d,r8,r1,s6/4,se,sf,s3/1,s6/5,sj,sh,r7,eg/a,r8,sg,ed/c,r0,sb,ej/i,s2/2,s0/2,s1/3,ed/a,m,sc,si,r3,s0/4,sb,m,r2,eg/g,si,s4/1,m,s3/1,ef/a,m,ee/g,ee/d,eg/e,r3,s8/7,eh/f,m,ea/g,sg,s3/0,s0/9,m,m,r7,r5,ec/a,sh,s0/5,si,sg,s9/6,sj,s0/1,r8,si,sc,s0/0,m,se,m,s3/6,m,m,m,ei/i,si,r5,m,r7,sh,s8/7,r7,s1/0,s7/6,r8,r5,ed/d,sj,sb,r8,s4/1,ee/h,s7/5,s9/9,sh,r3,s8/1,m,ei/b,s0/6,s0/7,s2/5,s4/9,r6,sf,ej/i,sj,sh,m,sg,sj,r5,sg,ed/b,r2,r4,s0/3,sb,sd,r2,ed/c,m,ef/c,s5/1,s2/0,m,si,r1,si,ef/i,si,r1,r6,sj,m,m,ed/c,sh,sf,sd,ej/j,s3/7,eg/i,sd,s2/0,s2/4,ee/c,ee/a,si,m,r1,m,ed/f,m,r2,ee/c,s0/9,ee/d,m,m,m,r5,sh,ec/f,se,si,m,ei/b,sc,r7,eb/c,se,m,ea/b,r4,s7/1,sg,s7/8,ee/c,s5/3,m,sd,s2/2,m,r7,s4/9,m,m,ea/i,s1/2,r3,sb,s0/0,sb,sj,ed/g,ef/j,r8,eg/f,s3/0,eh/f,sd,r7,s4/0,sc,sj,ef/h,r3,ee/b,r0,r4,s9/0,r0,m,r7,m,r6,r2,r1,sh,r8,m,r4,sh,m,sh,m,s2/5,se,sh,m,sc,ed/i,m,r8,m,r3,r8,m,sf,r6,m,s5/6,ei/d,m,r6,m,r3,sg,m,s1/0,sb,eg/g,m",
    )
)
