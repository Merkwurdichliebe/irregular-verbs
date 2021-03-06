VERBS = [
    ('arise', ('arose',), ('arisen',)),
    ('awake', ('awoke',), ('awoken',)),
    ('be', ('was', 'were'), ('been',)),
    ('bear', ('bore',), ('borne', 'born')),
    ('beat', ('beat',), ('beaten', 'beat')),
    ('become', ('became',), ('become',)),
    ('begin', ('began',), ('begun',)),
    ('bend', ('bent',), ('bent',)),
    ('bet', ('bet', 'betted'), ('bet', 'betted')),
    ('bind', ('bound',), ('bound',)),
    ('bite', ('bit',), ('bitten',)),
    ('bleed', ('bled',), ('bled',)),
    ('blow', ('blew',), ('blown',)),
    ('break', ('broke',), ('broken',)),
    ('bring', ('brought',), ('brought',)),
    ('build', ('built',), ('built',)),
    ('burn', ('burned', 'burnt'), ('burned', 'burnt')),
    ('burst', ('burst',), ('burst',)),
    ('buy', ('bought',), ('bought',)),
    ('cast', ('cast',), ('cast',)),
    ('catch', ('caught',), ('caught',)),
    ('choose', ('chose',), ('chosen',)),
    ('cling', ('clung',), ('clung',)),
    ('come', ('came',), ('come',)),
    ('cost', ('cost',), ('cost',)),
    ('creep', ('crept',), ('crept',)),
    ('cut', ('cut',), ('cut',)),
    ('deal', ('dealt',), ('dealt',)),
    ('dig', ('dug',), ('dug',)),
    ('dive', ('dived', 'dove'), ('dived')),
    ('do', ('did',), ('done',)),
    ('draw', ('drew',), ('drawn',)),
    ('dream', ('dreamed', 'dreamt'), ('dreamed', 'dreamt')),
    ('drink', ('drank',), ('drunk',)),
    ('drive', ('drove',), ('driven',)),
    ('eat', ('ate',), ('eaten',)),
    ('fall', ('fell',), ('fallen',)),
    ('feed', ('fed',), ('fed',)),
    ('feel', ('felt',), ('felt',)),
    ('fight', ('fought',), ('fought',)),
    ('find', ('found',), ('found',)),
    ('flee', ('fled',), ('fled',)),
    ('fling', ('flung',), ('flung',)),
    ('fly', ('flew',), ('flown',)),
    ('forbid', ('forbade',), ('forbidden',)),
    ('forget', ('forgot',), ('forgotten',)),
    ('forgive', ('forgave',), ('forgiven',)),
    ('forgo', ('forwent',), ('forgone',)),
    ('freeze', ('froze',), ('frozen',)),
    ('get', ('got',), ('gotten',)),
    ('give', ('gave',), ('given',)),
    ('go', ('went',), ('gone',)),
    ('grind', ('ground',), ('ground',)),
    ('grow', ('grew',), ('grown',)),
    ('hang', ('hung', 'hanged'), ('hung', 'hanged')),
    ('have', ('had',), ('had',)),
    ('hear', ('heard',), ('heard',)),
    ('hide', ('hid',), ('hidden',)),
    ('hit', ('hit',), ('hit',)),
    ('hold', ('held',), ('held',)),
    ('hurt', ('hurt',), ('hurt',)),
    ('keep', ('kept',), ('kept',)),
    ('kneel', ('knelt', 'kneeled'), ('knelt', 'kneeled')),
    ('knit', ('knitted', 'knit'), ('knitted', 'knit')),
    ('know', ('knew',), ('known',)),
    ('lay', ('laid',), ('laid',)),
    ('lead', ('led',), ('led',)),
    ('leap', ('leapt', 'leaped'), ('leapt', 'leaped')),
    ('leave', ('left',), ('left',)),
    ('lend', ('lent',), ('lent',)),
    ('let', ('let',), ('let',)),
    ('lie', ('lay',), ('lain',)),
    ('light', ('lit', 'lighted'), ('lit', 'lighted')),
    ('lose', ('lost',), ('lost',)),
    ('make', ('made',), ('made',)),
    ('mean', ('meant',), ('meant',)),
    ('meet', ('met',), ('met',)),
    ('pay', ('paid',), ('paid',)),
    ('prove', ('proved',), ('proved', 'proven')), 
    ('put', ('put',), ('put',)),
    ('quit', ('quit',), ('quit',)),
    ('read', ('read',), ('read',)),
    ('ride', ('rode',), ('ridden',)),
    ('ring', ('rang',), ('rung',)),
    ('rise', ('rose',), ('risen',)),
    ('run', ('ran',), ('run',)),
    ('saw', ('sawed',), ('sawed', 'sawn')),
    ('say', ('said',), ('said',)),
    ('see', ('saw',), ('seen',)),
    ('seek', ('sought',), ('sought',)),
    ('sell', ('sold',), ('sold',)),
    ('send', ('sent',), ('sent',)),
    ('set', ('set',), ('set',)),
    ('sew', ('sewed',), ('sewn',)),
    ('shake', ('shook',), ('shaken',)),
    ('shave', ('shaved',), ('shaved', 'shaven')), 
    ('shear', ('sheared',), ('sheared', 'shorn')),
    ('shine', ('shone', 'shined'), ('shone', 'shined')),
    ('shoot', ('shot',), ('shot',)),
    ('show', ('showed',), ('shown', 'showed')),
    ('shrink', ('shrank', 'shrunk'), ('shrunk', 'shrunken')),
    ('shut', ('shut',), ('shut',)),
    ('sing', ('sang',), ('sung',)),
    ('sink', ('sank',), ('sunk',)),
    ('sit', ('sat',), ('sat',)),
    ('slay', ('slew',), ('slain',)),
    ('sleep', ('slept',), ('slept',)),
    ('slide', ('slid',), ('slid',)),
    ('sneak', ('sneaked', 'snuck'), ('sneaked', 'snuck')),
    ('speak', ('spoke',), ('spoken',)),
    ('speed', ('sped',), ('sped',)),
    ('spend', ('spent',), ('spent',)),
    ('spill', ('spilled', 'spilt'), ('spilled', 'spilt')),
    ('spin', ('spun',), ('spun',)),
    ('spit', ('spat', 'spit'), ('spat', 'spit')),
    ('split', ('split',), ('split',)),
    ('spread', ('spread',), ('spread',)),
    ('spring', ('sprang',), ('sprung',)),
    ('stand', ('stood',), ('stood',)),
    ('steal', ('stole',), ('stolen',)),
    ('stick', ('stuck',), ('stuck',)),
    ('sting', ('stung',), ('stung',)),
    ('stink', ('stank', 'stunk'), ('stunk',)),
    ('strew', ('strewed',), ('strewn',)),
    ('strike', ('struck',), ('struck', 'stricken')),
    ('strive', ('strove', 'strived'), ('striven', 'strived')),
    ('swear', ('swore',), ('sworn',)),
    ('sweep', ('swept',), ('swept',)),
    ('swim', ('swam',), ('swum',)),
    ('swing', ('swung',), ('swung',)),
    ('take', ('took',), ('taken',)),
    ('teach', ('taught',), ('taught',)),
    ('tear', ('tore',), ('torn',)),
    ('tell', ('told',), ('told',)),
    ('think', ('thought',), ('thought',)),
    ('throw', ('threw',), ('thrown',)),
    ('undergo', ('underwent',), ('undergone',)),
    ('understand', ('understood',), ('understood',)),
    ('upset', ('upset',), ('upset',)),
    ('wake', ('woke',), ('woken',)),
    ('wear', ('wore',), ('worn',)),
    ('weave', ('wove',), ('woven',)),
    ('weep', ('wept',), ('wept',)),
    ('win', ('won',), ('won',)),
    ('wind', ('wound',), ('wound',)),
    ('withdraw', ('withdrew',), ('withdrawn',)),
    ('wring', ('wrung',), ('wrung',))
]