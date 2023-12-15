import cnocr


def init_ocr(model_name='densenet_lite_136-gru'):
    ocr = cnocr.CnOcr(model_name=model_name)
    return ocr


def _is_chinese(uchar):
    if '\u4e00' <= uchar <= '\u9fa5':
        return True
    else:
        return False


def _extract_chinese(string):
    s = ''
    for i in string:
        if i in [' ', '·', '丨', '丶', '丿', '乀', '乁', '乚']:
            continue
        if _is_chinese(i):
            s += i
    if s[-1] == '心':
        s = s[:-1]
    return s


def Ocr(ocr, img):
    try:
        result = ocr.ocr(img)[0]['text']
    except IndexError:
        return ''
    return _extract_chinese(result)


def Ocr_single_line(ocr, img):
    try:
        result = ocr.ocr_for_single_line(img)['text']
    except IndexError:
        return ''
    return result
