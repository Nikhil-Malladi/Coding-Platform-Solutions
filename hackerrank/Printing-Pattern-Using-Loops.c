#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int inp;
    scanf("%d",&inp);
    for(int x=inp;x>=1;x--)
    {
        for(int i=inp;i>=1;i--)
            {
                if(i<x)
                {
                    printf("%d ",x);
                }
                else
                {
                    printf("%d ",i);
                }
            }
        for(int j=2;j<=inp;j++)
            {
                if(j<x)
                {
                    printf("%d ",x);
                }
                else
                {
                    printf("%d ",j);
                }
            }
    printf("\n");
    }
    for(int y=2;y<=inp;y++)
        {
        for(int i=inp;i>=1;i--)
            {
                if(i<y)
                {
                    printf("%d ",y);
                }
                else
                {
                    printf("%d ",i);
                }
            }
        for(int j=2;j<=inp;j++)
            {
                if(j<y)
                {
                    printf("%d ",y);
                }
                else
                {
                    printf("%d ",j);
                }
            }
    printf("\n");
    }
}
