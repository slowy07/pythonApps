def diff(a, b):
    return a -b


def simpleColor(r,g,b):
    r = int(r)
    g = int(g)
    b = int(b)
    bg = ir = 0
    try:
        if r > g and r > b:
            rg = diff(r,g)
            rb = diff(r,b)
            
            if g < 65 and b < 65 and rg < 60:
                return "RED"
            
            gb = diff(g,b)
            if rg < rb:
                if gb < rg:
                    if gb >=30 and rg >=80:
                        return "ORANGE"
                    elif gb <=20 and rg >= 80:
                        return "RED"
                    elif gb <=20 and b > 175:
                        return "CREAM"
                    else:
                        return "COCHOLATE"
                else:
                    if rg > 60:
                        return "ORANGE"
                    elif r > 125:
                        return "AMARILLO"
                    else:
                        return "COCHOLATE"
            elif rg > rb:
                if bg > rb:
                    if gb < 60:
                        if r > 150:
                            return "RED 2"
                        else:
                            return "MARRON"
                    elif g > 125:
                        return "PINK"
                    else:
                        return "RED 3"
                else:
                    if rb > 60:
                        if r > 160:
                            return "PINK"
                        else:
                            return "RED"
                    else:
                        return "RED"
            else:
                if rg > 20:
                    if r >= 100 and b >= 60:
                        return "RED"
                    elif r >= 100:
                        return "RED"
                    else:
                        return "MARRON"
                else:
                    return "GRAY"
        
        elif g > r and g > b:
            gb = diff(g,b)
            gr = diff(g,r)
            
            if r < 65 and b < 65 and gb > 60:
                return "GREEN"
            
            rb = diff(r,b)
            if r > b:
                if gr < gb:
                    if rb >=150 and gr <= 20:
                        return "AMARILLO"
                    else:
                        return "GREEN"
                else:
                    return "GREEN"
            elif r > b:
                if gb < gr:
                    if gb <= 20:
                        return "turqoise"
                    else:
                        return "GREEN"
                else:
                    return "GREEN"
        
        elif b > r and b > g:
            bg = diff(b,g)
            br = diff(b,r)

            if r < 65 and g < 65 and bg > 60:
                return "BLUE"
            
            rg = diff(r,g)
            if g > r:
                if bg > rg:
                    if bg <= 20:
                        return "TURQOISE"
                    else:
                        return "LIGHT BLUE"
                else:
                    if rg <= 20:
                        if r <= 150:
                            return "LILAC"
                        else:
                            return "BLUE"
                    else:
                        return "BLUE"
            elif g > r:
                if br < rg:
                    if br <= 20:
                        if r > 50 and g < 75:
                            return "PINK"
                        elif ir > 150:
                            return "LILAC"
                        else:
                            return "purple"
                    else:
                        return "PURPLE"
                else:
                    if rg <= 20:
                        if bg <= 20:
                            return "GRAY"
                        else:
                            return "BLUE"
            else:
                if rg <= 20:
                    if r >= 100 and b > 60:
                        return "RED"
                    elif r >= 100:
                        return "RED"
                    else:
                        return "MARRON"
                else:
                    return "GRAY"
            
        else:
            return "GRAY"
    
    except:
        return "Not Color"


if __name__ == "__main__":
    import sys
    print(simpleColor(sys.argv[1], sys.argv[2], sys.argv[3]))
