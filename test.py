from main import *

if __name__ == "__main__":
    print(bin(0))
    print(bin(63))
    print(bin(63^2))

    assert(Chessboard.convertStringToXY("A1") == (0,0))
    assert(Chessboard.convertXYtoString((1,2)) == "B3")
    game = Game()
    assert(game.getBinaryEncoding(2, 3) == 26)
    assert(game.getBinaryEncoding(7, 7) == 63)
    print("Board value is  " + format(game.calculateBoardValue(), '#008b'))
    print("Key encoding is " + format(game.getKeyEncoding(), '#008b'))
    print(f"Flip location is {game.calculateFlipLocation()}")
    x, y = game.calculateFlipLocation()
    print(f"Which is binary: " + format(game.getBinaryEncoding(x, y), '#008b'))
    temp = Chessboard.convertXYtoString(game.calculateFlipLocation())
    game.flipCoin(temp)
    print("After flip, board encoding is:" + format(game.calculateBoardValue(), '#008b'))
    assert(game.calculateBoardValue() == game.getKeyEncoding())