#!/usr/bin/env python3
"""Render the profile's original motion artwork. Optional: pip install Pillow numpy.

All uploaded assets are already built. GitHub Actions does NOT need these packages.
Run from anywhere: python scripts/render-assets.py
"""
from pathlib import Path
import math
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets'
FONTS = Path(__file__).parent / 'fonts'
S = 2
BG = '#090e19'
PANEL = '#0f1827'
LINE = '#243145'
WHITE = '#f1f5ff'
MUTED = '#a1b0c8'
DIM = '#64758f'
MINT = '#b8f780'
CYAN = '#72dfee'
VIOLET = '#b4a5ff'
FRAMES = 96
TWO_PI = math.pi * 2


def font(size, weight='regular'):
    names = {'regular': 'OpenSans-Regular.ttf', 'light': 'OpenSans-Light.ttf',
             'bold': 'OpenSans-Semibold.ttf', 'mono': 'DejaVuSansMono.ttf'}
    return ImageFont.truetype(str(FONTS / names[weight]), round(size*S))


def text(d, xy, value, size=20, color=WHITE, weight='regular', anchor=None):
    d.text(tuple(round(n*S) for n in xy), value, font=font(size, weight),
           fill=color, anchor=anchor, stroke_width=0)


def line(d, points, color=LINE, width=1):
    d.line([(round(x*S),round(y*S)) for x,y in points], fill=color, width=round(width*S))


def rr(d, bounds, radius=12, fill=PANEL, outline=LINE, width=1):
    d.rounded_rectangle(tuple(round(v*S) for v in bounds), round(radius*S),
                        fill=fill, outline=outline, width=round(width*S))


def circle(d, x,y,r, fill=None, outline=None, width=1):
    d.ellipse(((x-r)*S,(y-r)*S,(x+r)*S,(y+r)*S), fill=fill, outline=outline,width=round(width*S))


def canvas(w,h,glow=True):
    yy,xx=np.mgrid[:h*S,:w*S]
    rgb=np.zeros((h*S,w*S,3),dtype=np.float32)+np.array([9,14,25])
    if glow:
        a=np.exp(-(((xx/S-w*.82)/(w*.28))**2+((yy/S-h*.36)/(h*.74))**2)*2.5)
        b=np.exp(-(((xx/S-w*.62)/(w*.30))**2+((yy/S-h*.95)/(h*.65))**2)*3.5)
        rgb+=a[:,:,None]*np.array([13,15,31])+b[:,:,None]*np.array([2,15,18])
    im=Image.fromarray(np.uint8(np.clip(rgb,0,255)))
    d=ImageDraw.Draw(im)
    rr(d,(1,1,w-2,h-2),22,fill=None,outline=LINE)
    return im


def pill(d,x,y,label,color=MINT,size=16):
    f=font(size,'mono')
    width=d.textlength(label,font=f)/S+32
    rr(d,(x,y,x+width,y+38),19,fill=PANEL,outline=LINE)
    text(d,(x+16,y+8),label,size,color,'mono')
    return width


def arrow(d,x,y,color=MINT,size=13):
    line(d,[(x-size,y+size),(x+size,y-size)],color,2)
    line(d,[(x-size+4,y-size),(x+size,y-size),(x+size,y+size-4)],color,2)


def react(d,cx,cy,r,color=CYAN,rotation=0,width=1.8):
    for angle in (0,math.pi/3,-math.pi/3):
        pts=[]
        for k in range(101):
            theta=k/100*TWO_PI
            x=r*math.cos(theta);y=r*.36*math.sin(theta)
            a=angle+rotation
            pts.append((cx+x*math.cos(a)-y*math.sin(a),cy+x*math.sin(a)+y*math.cos(a)))
        line(d,pts,color,width)
    circle(d,cx,cy,r*.105,fill=color)


def orbit(d,cx,cy,t,r=135):
    for ri in (r-37,r,r+31):
        circle(d,cx,cy,ri,outline='#28374c',width=1)
    # Fine tilted orbital paths and traveling particles; all paths loop cleanly.
    for j,angle in enumerate((-.4,.65)):
        pts=[]
        for k in range(145):
            a=k/144*TWO_PI
            x=(r+25)*math.cos(a);y=(r*.48)*math.sin(a)
            pts.append((cx+x*math.cos(angle)-y*math.sin(angle),cy+x*math.sin(angle)+y*math.cos(angle)))
        line(d,pts,'#3b4862',1)
        a=t*TWO_PI*(1 if j==0 else -1)+j*2
        x=(r+25)*math.cos(a);y=r*.48*math.sin(a)
        px=cx+x*math.cos(angle)-y*math.sin(angle);py=cy+x*math.sin(angle)+y*math.cos(angle)
        circle(d,px,py,8,fill='#1d3943' if j==0 else '#34304b')
        circle(d,px,py,3.2,fill=CYAN if j==0 else VIOLET)
    rr(d,(cx-59,cy-59,cx+59,cy+59),26,fill='#111c2b',outline='#526450')
    text(d,(cx,cy-8),'AF',45,MINT,'light',anchor='mm')
    text(d,(cx,cy+30),'</>',16,DIM,'mono',anchor='mm')


def typed(t):
    messages=('Design the interface.','Connect the API.','Ship the experience.')
    phase=t*3; idx=int(phase)%3; p=phase%1
    # Enter, hold, delete; keep the animation within one fixed text area.
    n=int(min(1,p/.27)*len(messages[idx])) if p<.78 else int((1-p)/.22*len(messages[idx]))
    return messages[idx][:max(0,n)] + ('_' if int(t*24)%2==0 else ' ')


def hero_frame(t,mobile=False):
    w,h=(760,920) if mobile else (1280,560)
    im=canvas(w,h);d=ImageDraw.Draw(im)
    x=44 if mobile else 54
    rr(d,(x,32,x+39,71),10,fill='#1b2a24',outline='#344c35')
    text(d,(x+8,39),'AF',17,MINT,'bold')
    text(d,(x+55,35),'MD. ABRAR FAHIM',15,WHITE,'mono')
    text(d,(x+55,57),'@abrarfahimabir',12,DIM,'mono')
    if not mobile:
        circle(d,1005,52,3.5,fill=MINT)
        text(d,(1020,43),'DHAKA / BANGLADESH',13,MUTED,'mono')
    line(d,[(x,94),(w-x,94)])
    text(d,(x,128),'REACT + DJANGO DEVELOPER',16,MINT,'mono')
    text(d,(x-5,171),'Abrar Fahim.',77 if mobile else 82,WHITE,'bold')
    text(d,(x,285),'Good interfaces.',35,WHITE,'light')
    text(d,(x,330),'Solid foundations.',35,MUTED,'light')
    pill(d,x,413,'REACT',CYAN)
    pill(d,x+120,413,'DJANGO',MINT)
    pill(d,x+251,413,'REST APIs',VIOLET)
    if mobile:
        orbit(d,380,660,t,130)
        text(d,(380,828),typed(t),19,CYAN,'mono',anchor='mm')
        line(d,[(x,869),(w-x,869)])
        text(d,(x,888),'CSE @ GREEN UNIVERSITY OF BANGLADESH',13,MUTED,'mono')
    else:
        # Blueprint grid, restricted to the artwork half of the banner.
        for gx in range(800,1230,36):
            for gy in range(126,446,36): circle(d,gx,gy,.8,fill='#2b3649')
        orbit(d,1010,283,t)
        rr(d,(807,431,1211,470),10,fill='#101c2a',outline='#2b4255')
        text(d,(827,441),'› '+typed(t),16,CYAN,'mono')
        line(d,[(x,499),(w-x,499)])
        text(d,(x,518),'CSE @ GREEN UNIVERSITY OF BANGLADESH',12,MUTED,'mono')
        text(d,(w-x,518),'INTERFACE  /  API  /  EXPERIENCE',12,DIM,'mono',anchor='ra')
    return im


def flow_frame(t):
    im=canvas(1280,246);d=ImageDraw.Draw(im)
    text(d,(40,28),'ONE STACK. END TO END.',14,MINT,'mono')
    text(d,(1240,28),'HOW I BUILD',12,DIM,'mono',anchor='ra')
    nodes=[(40,'01','THE INTERFACE','React','Components · state · motion',CYAN),
           (473,'02','THE API','Django','Auth · permissions · REST',MINT),
           (905,'03','THE DATA','Database','Models · queries · storage',VIOLET)]
    for x,num,over,title,sub,color in nodes:
        rr(d,(x,77,x+335,207),14,fill='#111b2a',outline='#2c394b')
        text(d,(x+20,95),over,11,DIM,'mono')
        text(d,(x+20,115),title,27,WHITE,'bold')
        text(d,(x+20,168),sub,11,MUTED,'regular')
        if title=='React':react(d,x+289,135,23,color,rotation=t*math.pi/3)
        elif title=='Django':text(d,(x+270,110),'dj',35,color,'bold')
        else:
            for sy in (123,137,151):
                d.ellipse(((x+268)*S,(sy-7)*S,(x+308)*S,(sy+7)*S),fill=PANEL,outline=color,width=2)
            line(d,[(x+268,123),(x+268,151)],color);line(d,[(x+308,123),(x+308,151)],color)
    for a,b,offset in [(375,473,0),(808,905,.5)]:
        line(d,[(a+8,143),(b-8,143)],'#384b5a',1.5)
        p=(t*2+offset)%1
        for j in range(4):
            px=a+8+(b-a-16)*((p-j*.07)%1)
            circle(d,px,143,2.4-j*.35,fill=CYAN if j==0 else '#3b626b')
    return im


def lms_visual(d,x,y,t):
    rr(d,(x,y,x+430,y+230),15,fill='#0e1826',outline='#354756')
    line(d,[(x,y+36),(x+430,y+36)],'#2a394b')
    for i,c in enumerate(('#b4a5ff','#72dfee','#b8f780')):circle(d,x+18+i*14,y+18,3,fill=c)
    text(d,(x+86,y+11),'skillstream / learning',10,DIM,'mono')
    rr(d,(x+16,y+52,x+104,y+211),8,fill='#162032',outline=None)
    text(d,(x+27,y+65),'LEARN',9,CYAN,'mono')
    for i,label in enumerate(('Courses','Lessons','Progress')):
        text(d,(x+27,y+99+i*31),label,9,WHITE if i==0 else DIM)
    text(d,(x+124,y+58),'Keep moving forward.',15,WHITE,'bold')
    text(d,(x+124,y+87),'COURSE → MODULE → LESSON',8,DIM,'mono')
    for i in range(3):
        yy=y+117+i*29
        circle(d,x+131,yy+7,6,fill='#254535',outline='#436044')
        line(d,[(x+128,yy+7),(x+131,yy+10),(x+135,yy+4)],MINT,1)
        rr(d,(x+148,yy,x+397,yy+13),6,fill='#1d2a3a',outline=None)
        length=100+100*(.5+.5*math.sin((t-i*.15)*TWO_PI))
        rr(d,(x+148,yy,x+148+length,yy+13),6,fill=(CYAN,MINT,VIOLET)[i],outline=None)
    text(d,(x+124,y+209),'STUDENT  /  INSTRUCTOR  /  ADMIN',8,DIM,'mono')


def blog_visual(d,x,y,t):
    rr(d,(x,y,x+430,y+230),15,fill='#0e1826',outline='#354756')
    text(d,(x+22,y+18),'POST VISIBILITY',11,VIOLET,'mono')
    line(d,[(x+22,y+48),(x+408,y+48)])
    labels=('Everyone','Only me','Selected users')
    selected=int(t*3)%3
    for i,label in enumerate(labels):
        yy=y+65+i*48
        rr(d,(x+20,yy,x+410,yy+37),9,fill='#201f37' if i==selected else '#111c2b',
           outline='#746a9d' if i==selected else '#263448')
        circle(d,x+40,yy+19,6,outline=VIOLET if i==selected else DIM)
        if i==selected:circle(d,x+40,yy+19,2.8,fill=VIOLET)
        text(d,(x+61,yy+9),label,13,WHITE if i==selected else MUTED)
        if i==selected:line(d,[(x+377,yy+19),(x+382,yy+23),(x+390,yy+14)],VIOLET,1.8)
    line(d,[(x+23,y+218),(x+407,y+218)],'#28374c')
    circle(d,x+23+384*(.5-.5*math.cos(t*TWO_PI)),y+218,3,fill=VIOLET)


def project_frame(t,kind):
    im=canvas(1280,336);d=ImageDraw.Draw(im)
    lms=kind=='skillstream';accent=CYAN if lms else VIOLET
    text(d,(42,28),'01 / FULL-STACK LMS' if lms else '02 / DJANGO APPLICATION',13,accent,'mono')
    text(d,(40,70),'SkillStream' if lms else 'Ostad Blog',48,WHITE,'bold')
    text(d,(42,146),'A clearer path from course to completion.' if lms else 'Your words. Your audience. Your rules.',21,MUTED,'light')
    text(d,(42,195),'REACT + DJANGO REST FRAMEWORK' if lms else 'DJANGO + PYTHON + BOOTSTRAP',12,accent,'mono')
    text(d,(42,233),'Courses · role-based access · lesson progress' if lms else 'Authentication · author controls · post visibility',14,WHITE)
    text(d,(42,289),'EXPLORE THE CODE',12,DIM,'mono');arrow(d,225,296,accent,7)
    (lms_visual if lms else blog_visual)(d,807,52,t)
    return im


def contact_frame(t):
    im=canvas(1280,193);d=ImageDraw.Draw(im)
    text(d,(42,25),'LET’S BUILD SOMETHING USEFUL.',13,MINT,'mono')
    text(d,(40,60),'Have an idea? Let’s talk.',39,WHITE,'light')
    text(d,(42,132),'dev.abrarfahim@gmail.com',17,MUTED,'mono')
    circle(d,1177,97,44,fill='#192c25',outline='#3d5b3d')
    arrow(d,1177,97,MINT,15)
    # A low-contrast orbital dot; restrained motion keeps the email readable.
    a=t*TWO_PI;circle(d,1177+55*math.cos(a),97+55*math.sin(a),3.5,fill=CYAN)
    return im


def finish(im):
    return im.resize((im.width//S,im.height//S),Image.Resampling.LANCZOS)


def save_animation(name,fn,count=FRAMES):
    print('Rendering',name,flush=True)
    raw=[finish(fn(i/count)) for i in range(count)]
    # A single palette prevents temporal dithering/shimmer in still typography.
    samples=[raw[i].resize((320,max(1,round(raw[i].height*320/raw[i].width)))) for i in range(0,count,12)]
    sheet=Image.new('RGB',(320,sum(s.height for s in samples)))
    y=0
    for sample in samples:sheet.paste(sample,(0,y));y+=sample.height
    palette=sheet.quantize(colors=128,method=Image.Quantize.MEDIANCUT)
    # Preserve small brand accents that a dark-background histogram can miss.
    from PIL import ImageColor
    values=palette.getpalette()[:128*3]
    base=np.array(ImageColor.getrgb(BG))
    for color in (WHITE,MINT,CYAN,VIOLET,MUTED,DIM,LINE,PANEL):
        end=np.array(ImageColor.getrgb(color))
        for alpha in np.linspace(0,1,16):
            values.extend(np.uint8(base*(1-alpha)+end*alpha).tolist())
    palette.putpalette(values)
    frames=[im.quantize(palette=palette,dither=Image.Dither.NONE) for im in raw]
    frames[0].save(OUT/(name+'.gif'),save_all=True,append_images=frames[1:],
                   duration=80,loop=0,optimize=True,disposal=1)
    # Pick a fully populated frame for browsers requesting less animation.
    raw[round(count*.15)].save(OUT/(name+'-still.png'),optimize=True)
    print(name,round((OUT/(name+'.gif')).stat().st_size/1024),'KiB',flush=True)


def button(filename,label,primary=False,width=220):
    im=Image.new('RGB',(width*S,50*S),BG);d=ImageDraw.Draw(im)
    rr(d,(1,1,width-2,48),11,fill=MINT if primary else PANEL,outline=MINT if primary else '#40516a')
    text(d,(17,13),label,16,'#152115' if primary else WHITE,'bold')
    arrow(d,width-25,25,'#152115' if primary else CYAN,6)
    finish(im).save(OUT/filename,optimize=True)


if __name__=='__main__':
    OUT.mkdir(exist_ok=True)
    names=set(sys.argv[1:])
    jobs=[('hero',lambda t:hero_frame(t)),('hero-mobile',lambda t:hero_frame(t,True)),
          ('stack-flow',flow_frame),('skillstream',lambda t:project_frame(t,'skillstream')),
          ('ostad-blog',lambda t:project_frame(t,'blog')),('contact',contact_frame)]
    for name,fn in jobs:
        if not names or name in names:save_animation(name,fn)
    button('button-portfolio.png','View portfolio',True,207)
    button('button-email.png','Get in touch',False,196)
    button('button-repositories.png','Explore repositories',False,265)
