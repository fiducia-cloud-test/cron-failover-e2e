#!/usr/bin/env python3

def apply_fire(consumed: bool) -> tuple[bool, int]:
    if consumed:
        return True, 0
    return True, 1

def main() -> None:
    consumed = False
    effects = 0
    for _ in range(3):
        consumed, delta = apply_fire(consumed)
        effects += delta
    assert consumed
    assert effects == 1, 'duplicate schedule effect observed'
    print('schedule firing model: 3 retries, exactly one effect')

if __name__ == '__main__':
    main()
