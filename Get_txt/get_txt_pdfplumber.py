import pdfplumber


def not_within_bboxes(obj):
    """Check if the object is in any of the table's bbox."""

    def obj_in_bbox(_bbox):
        """See https://github.com/jsvine/pdfplumber/blob/stable/pdfplumber/table.py#L404"""
        v_mid = (obj["top"] + obj["bottom"]) / 2
        h_mid = (obj["x0"] + obj["x1"]) / 2
        x0, top, x1, bottom = _bbox
        return (h_mid >= x0) and (h_mid < x1) and (v_mid >= top) and (v_mid < bottom)

    return not any(obj_in_bbox(__bbox) for __bbox in bboxes)


with pdfplumber.open("./data/test2.pdf") as pdf:
    for page in pdf.pages:
        bboxes = [
            table.bbox
            for table in page.find_tables(
                table_settings={
                    "vertical_strategy": "text",
                    "horizontal_strategy": "lines",
                    "explicit_vertical_lines": page.curves + page.edges,
                    "explicit_horizontal_lines": page.curves + page.edges,
                }
            )
        ]

        print("\n\n\n\n\nText outside the tables:")
        print(page.filter(not_within_bboxes).extract_text())