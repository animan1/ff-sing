from richenum import OrderedRichEnum, OrderedRichEnumValue


class Position(OrderedRichEnum):
    RB = OrderedRichEnumValue(index=1, canonical_name="RB", display_name="RB")
    WR = OrderedRichEnumValue(index=2, canonical_name="WR", display_name="WR")
