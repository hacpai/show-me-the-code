#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <string.h>
#include <unistd.h>


int main()
{
    int socket_server = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in server_st, client_st;
    server_st.sin_family = AF_INET;
    server_st.sin_port = htons(8080);
    int ret = bind(socket_server, (struct sockaddr*)(&server_st), sizeof(struct sockaddr));
    ret = listen(socket_server, 10);
    socklen_t len = sizeof(struct sockaddr);
    int socket_client = accept(socket_server, (struct sockaddr *)(&client_st), &len);
    char data[16];
    int len_read = read(socket_client, data, sizeof(data));
    if (len_read > 0)
    {
        data[len_read] = '\0';
        printf("read:%s\n", data);
    }
    close(socket_client);
    close(socket_server);
    return 0;
}

