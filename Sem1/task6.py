''' Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
*Пример:*
385916 -> yes
123456 -> no '''

ticketNumber = input("Enter the ticket number: ")

if int(ticketNumber[0])+int(ticketNumber[1])+int(ticketNumber[2]) == int(ticketNumber[3])+int(ticketNumber[4])+int(ticketNumber[5]):
    print(f"Ticket with a number {ticketNumber} is happy")
else:
    print(
        f"Ticket with a number {ticketNumber} not happy, try to buy another ticket")
