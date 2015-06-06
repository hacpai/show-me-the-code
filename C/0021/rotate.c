#include <stdio.h>
#include <math.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <string.h>
#include <unistd.h>

#define PI 3.1415926535897932
#define rad(angle) ((angle)*PI/180.0)
#define SRC_SIZE (200*200)
#define DEST_SIZE (400*400)
#define BMP_HEAD 54
#define BMP_PIC "image.bmp"
#define SCREEN_SIZE (800*480)
#define BMP_WIDTH 200
#define BMP_HEIGHT 200
#define CIRCLE_ANGLE 360

static int screen[CIRCLE_ANGLE][DEST_SIZE];

int check_error(int pd, char str[]);
int w_pic(int *pfb, int *a, int x_sta, int y_sta, int w_pic, int h_pic);
int rotate(int *src, int screen[][DEST_SIZE], int angle, int num);
int compute_pic(int srceen[][DEST_SIZE], int src[]);
int display_pic(int screen[][DEST_SIZE], int *pfb);

int main(int argc, char const *argv[])
{
	
	int dest[DEST_SIZE] = {0};
	int src[SRC_SIZE] = {0};
	int fd = open("/dev/fb0",O_RDWR);
    check_error(fd, "open");

	int *pfb = (int *)mmap(NULL,SCREEN_SIZE*4,PROT_READ|PROT_WRITE,MAP_SHARED,fd,0);
    check_error(*pfb, "mmap");

    int pic = open(BMP_PIC,O_RDONLY);
    check_error(pic, "open");

	lseek(pic, BMP_HEAD, SEEK_SET);
	read(pic, src, SRC_SIZE*4);

	close(pic);

	memset(pfb, 0, SCREEN_SIZE*4);
	w_pic(pfb, src, 300, 340, BMP_WIDTH, BMP_HEIGHT);

    compute_pic(screen, src);
    display_pic(screen, pfb);

	return 0;
}

int check_error(int fb, char str[])
{
    if (fb < 0)
        perror(str);
    return -1;
}

int w_pic(int *pfb, int *a, int x_sta, int y_sta, int w_pic, int h_pic)
{   
  int i, j;

  for(i=0; i<h_pic; i++)    // next y
  {
    for(j=0; j<w_pic; j++)  // next x
    {
      *(pfb + (y_sta-i)*800 + x_sta+j ) = *(a + i*h_pic + j );
    }
  }
  return 0;
}

int rotate(int *src, int screen[][DEST_SIZE], int angle, int num)
{

	//int xo = 400, yo = 240;
	int xa, ya;
	float xoa, yoa, xob, yob;
	float sina, cosa;
	int xb, yb;
	if (angle >= CIRCLE_ANGLE)
	{
		angle = angle - (angle/CIRCLE_ANGLE)*CIRCLE_ANGLE;
	}
	else if (angle < 0)
	{
		angle = angle + ((0 - angle/CIRCLE_ANGLE)+1)*CIRCLE_ANGLE;
	}
	sina = (float)sin(rad(angle));
	cosa = (float)cos(rad(angle));
	for (xa = 0; xa < BMP_WIDTH; ++xa)
	 {
	 	for (ya = 0; ya < BMP_HEIGHT; ++ya)
	 	{
	 		xoa = xa -BMP_WIDTH/2;
	 		yoa = 0 - ya + BMP_HEIGHT/2;
	 		xob = xoa*cosa + yoa*sina;
	 		yob = yoa*cosa - xoa*sina;
	 		xb = xob +BMP_WIDTH;
			yb = 0 - yob + BMP_HEIGHT;
	 		screen[num][yb*400 + xb] = src[ya*BMP_HEIGHT + xa];
	 	}
	 }
	 return 0;
}

int compute_pic(int srceen[][DEST_SIZE], int src[])
{
    for (int i = 0; i < CIRCLE_ANGLE; i+=1)
        rotate(src, screen, i, i);
    return 0;
}

int display_pic(int screen[][DEST_SIZE], int *pfb)
{
	for (int i = 0; ; i += 1)
	{
		w_pic(pfb, screen[i], 200, 440, 400, 400); 
		if (i == CIRCLE_ANGLE)
			i = 0;
    }
    return 0;
}
