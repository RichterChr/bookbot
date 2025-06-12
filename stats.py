def word_count(booktext):
    words = booktext.split()
    num_words = len(words)
    print(f"{num_words} words found in the document")

def character_count(booktext):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0
    n = 0
    o = 0
    p = 0
    q = 0
    r = 0
    s = 0
    t = 0
    u = 0
    v = 0
    w = 0
    x = 0
    y = 0
    z = 0
    
    character_dict = {        
        "a" : a,
        "b" : b,
        "c" : c,
        "d" : d,
        "e" : e,
        "f" : f,
        "g" : g,
        "h" : h,
        "i" : i,
        "j" : j,
        "k" : k,
        "l" : l,
        "m" : m,
        "o" : o,
        "p" : p,
        "q" : q,
        "r" : r,
        "s" : s,
        "t" : t,
        "u" : u,
        "v" : v,
        "w" : w,
        "x" : x,
        "y" : y,
        "z" : z
        }
    
    lowercase = booktext.lower()
    for letter in lowercase:
        if letter == "a":
            a += 1
        elif letter == "b":
            b += 1
        elif letter == "c":
            c += 1
        elif letter == "d":
            d += 1
        elif letter == "e":
            e += 1
        elif letter == "f":
            f += 1
        elif letter == "g":
            g += 1
        elif letter == "h":
            h += 1
        elif letter == "i":
            i += 1
        elif letter == "j":
            j += 1
        elif letter == "k":
            k += 1
        elif letter == "l":
            l += 1
        elif letter == "m":
            m += 1
        elif letter == "n":
            n += 1
        elif letter == "o":
            o += 1
        elif letter == "p":
            p += 1
        elif letter == "q":
            q += 1
        elif letter == "r":
            r += 1
        elif letter == "s":
            s += 1
        elif letter == "t":
            t += 1
        elif letter == "u":
            u += 1
        elif letter == "v":
            v += 1
        elif letter == "w":
            w += 1
        elif letter == "x":
            x += 1
        elif letter == "y":
            y += 1
        elif letter == "z":
            z += 1
    character_dict["a"] = a
    character_dict["b"] = b
    character_dict["c"] = c
    character_dict["d"] = d
    character_dict["e"] = e
    character_dict["f"] = f
    character_dict["g"] = g
    character_dict["h"] = h
    character_dict["i"] = i
    character_dict["j"] = j
    character_dict["k"] = k
    character_dict["l"] = l
    character_dict["m"] = m
    character_dict["n"] = n
    character_dict["o"] = o
    character_dict["p"] = p
    character_dict["q"] = q
    character_dict["r"] = r
    character_dict["s"] = s
    character_dict["t"] = t
    character_dict["u"] = u
    character_dict["v"] = v
    character_dict["w"] = w
    character_dict["x"] = x
    character_dict["y"] = y
    character_dict["z"] = z
    print(character_dict)