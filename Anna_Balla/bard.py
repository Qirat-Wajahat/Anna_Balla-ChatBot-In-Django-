from bardapi import Bard

def bard_bot():
    bard = Bard(
        token='g.a000mwjyCt3y_Odv1e8C7dnOLsXrEoRtZjrJIT33MztcxHZmG4Q2Hfa6PMosdgIuZVuJiRwbQQACgYKAawSARYSFQHGX2MiTbI1QXFaK7bAfOVgigQc8xoVAUF8yKrEbxm4-_2OoG0lrJguHs7Y0076')
    bard_response = bard.get_answer(query)
    print(bard_response['content'])
    return bard_response['content']

    # bard = Bard(
    #     token='g.a000mwjyCt3y_Odv1e8C7dnOLsXrEoRtZjrJIT33MztcxHZmG4Q2Hfa6PMosdgIuZVuJiRwbQQACgYKAawSARYSFQHGX2MiTbI1QXFaK7bAfOVgigQc8xoVAUF8yKrEbxm4-_2OoG0lrJguHs7Y0076')
    # bard_response = bard.get_answer(query)
    # print(bard_response['content'])
    # return bard_response['content']
