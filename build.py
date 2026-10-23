import base64, pathlib
R = pathlib.Path(__file__).parent
m = 'data:image/png;base64,' + base64.b64encode((R/'sprites'/'base.png').read_bytes()).decode()
s = (R/'src'/'book.html').read_text().replace('__MASCOT__', m)
(R/'index.html').write_text(s); print('built', len(s)//1024, 'KB')
