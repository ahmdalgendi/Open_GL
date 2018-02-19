from Draw import *

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1000, 1000)
    glutCreateWindow(b'GENDY')
    glutDisplayFunc(draw)
    glutMainLoop()

main()