def convert_to_hsv(rgb):
    r,g,b = rgb[0]/255, rgb[1]/255, rgb[2]/255
    max_ = max(rgb)
    min_ = min(rgb)
    diff = max_ - min_

    if diff == 0:
        h = 0
    elif max_ == g:
        h = (60 * ((b - r) / diff) + 360) % 360
    elif max_ == r:
        h = (60 * ((g - b) / diff) + 360) % 360
    else:
        h = (60 * ((r - g) / diff) + 240) % 360

    if max_ == 0: 
        s = 0
    else: 
        s = (diff / max_) * 100
  
    # compute v 
    v = max_ * 100
    return h, s, v 



    


    
