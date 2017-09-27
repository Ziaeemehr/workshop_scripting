#ifndef NUMBER_H
#define NUMBER_H
class Number
{
public:
    Number(int start);
    ~Number(  );
    void add(int value);
    void sub(int value);
    void display(  );
    int data;
};

#endif