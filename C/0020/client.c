#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>

#define SERVER_IP "192.168.3.40"
#define SERVER_PORT 8888

int check_error(int ret_val, char type[]);
struct sockaddr_in init_address(int sin_port);

int main()
{
    int socket_fd = socket(AF_INET, SOCK_STREAM, 0);
    check_error(socket_fd, "socket");
    struct sockaddr_in server_st =  init_address(SERVER_PORT);
    int ret = connect(socket_fd, (struct sockaddr*)&server_st, sizeof(struct sockaddr));
    int msg_len;
    scanf("%d", &msg_len);
    char msg[msg_len];
    scanf("%s", msg);
    check_error(ret, "connect");
    write(socket_fd, msg, strlen(msg));
    close(socket_fd);
    return 0;
}

int check_error(int ret_val, char type[])
{
    if (ret_val < 0)
        perror(type);
    return ret_val;
}

struct sockaddr_in init_address(int sin_port)
{
    struct sockaddr_in server_st;
    server_st.sin_family = AF_INET;
    server_st.sin_port = htons(sin_port);
    inet_aton(SERVER_IP, &server_st.sin_addr);
    memset(server_st.sin_zero, 0, 8);
    return server_st;
}

