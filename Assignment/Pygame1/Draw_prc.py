import pygame
import itertools
import time

def draw_board(the_board):
    """ Draw a chess board with queens, as determined by the the_board. """
    pygame.init()
    colors = [(255,0,0), (0,0,0)]    # Set up colors [red, black]

    n = len(the_board)         # This is an NxN chess board.
    surface_sz = 480           # Proposed physical surface size.
    sq_sz = surface_sz // n    # sq_sz is length of a square.
    surface_sz = n * sq_sz     # Adjust to exactly fit n squares.

    # Create the surface of (width, height), and its window.
    surface = pygame.display.set_mode((surface_sz, surface_sz))

    ball = pygame.image.load("Queen.png")

    # Use an extra offset to centre the ball in its square.
    # If the square is too small, offset becomes negative,
    #   but it will still be centered :-)
    ball_offset = (sq_sz-ball.get_width()) // 2

    while True:

        # Look for an event from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;
        if ev.type==pygame.KEYDOWN:
            key=ev.dict["key"]
            if key==27:
                break
            if key==32:
                break
            if key==ord("r"):
                colors[0]=(255,0,0)
            elif key==ord('g'):
                colors[0]=(0,255,0)
            elif key==ord("b"):
                colors[0]=(0,0,255)

        # Draw a fresh background (a blank chess board)
        for row in range(n):           # Draw each row of the board.
            c_indx = row % 2           # Alternate starting color
            for col in range(n):       # Run through cols drawing squares
                the_square = (col*sq_sz, row*sq_sz, sq_sz, sq_sz)
                surface.fill(colors[c_indx], the_square)
                # Now flip the color index for the next square
                c_indx = (c_indx + 1) % 2

        # Now that squares are drawn, draw the queens.
        for (col, row) in enumerate(the_board):
            surface.blit(ball,(col*sq_sz+ball_offset,row*sq_sz+ball_offset))

        pygame.display.flip()


    pygame.quit()

'''if __name__ == "__main__":
    draw_board([6, 4, 2, 0, 5, 7, 1, 3])'''

def share_diagonal(x0,y0,x1,y1):
    dy=abs(y1-y0)
    dx=abs(x1-x0)
    return dx==dy
def col_clashes(bs,c):
    for i in range(c):
        if share_diagonal(i,bs[i],c,bs[c]):
            return True
    return False
def has_clashes(the_board):
    for col in range(1,len(the_board)):
        if col_clashes(the_board,col):
            return True
    return False
def main():
    #rng=random.Random()
    global no
    no=int(input("Number of queens: "))
    bd=list(range(no))
    num_found=0
    tries=0
    num=itertools.permutations(bd)
    global result
    result=[]
    for i in num:
        #rng.shuffle(bd)
        tries+=1
        if not has_clashes(i):
            #print("Found solution {0} in {1} tries.".format(i,tries))
            draw_board(i)
            tries=0
            num_found+=1
            result.append(list(i))


