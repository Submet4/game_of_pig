#Spielerklärung:
#Gewürfelt wird reihum mit zwei Würfeln. Es wird immer die geworfene Augensumme addiert. Jeder Spieler darf so oft würfeln, wie er möchte.
#Der Spieler, der zuerst 100 Punkte hat, ist Sieger.
#Wird allerdings eine 1 geworfen, erhält der Spieler 0 Punkte in der Runde und muss die Würfel weitergeben.
#Werden sogar zwei Einsen
#geworfen, wird die Gesamtpunktzahl auf 0 zurückgesetzt und der Würfel weitergegeben.
#

#Initialisierung

player1_score = 0
player2_score = 0

goal_score = 30

ongoing_round_score = 5

player1_score = player1_score + ongoing_round_score

print(player1_score)
