import requests

url = [
    "https://docs.google.com/forms/d/e/1FAIpQLSeT5IB0STSo4sdkGxoTQndwAfvRUiHwY9LzesQxxVRsCaWLTQ/formResponse","https://docs.google.com/forms/d/e/1FAIpQLSdZtn4xHrbMFSgjnCqV17PtoiJWInukZD2fM2HeQXr2SLxKWg/formResponse",
       "https://docs.google.com/forms/d/e/1FAIpQLSfwQANMWD8rHbZ3LuA2lxQUZsjSA8mF0snsJQdoVG3XSnNe8A/formResponse","https://docs.google.com/forms/d/e/1FAIpQLSeBIiutnf4vuYJFC7OUU74JHC9FCtIzvmzgL853TD9PG_V47g/formResponse","https://docs.google.com/forms/d/e/1FAIpQLSd8la2MJ3Vn-q8Uppz1vEsUuF2jxn6OIG5HUlnqKk6atu0NlA/formResponse","https://docs.google.com/forms/d/e/1FAIpQLSdEKVydKLGcb6LAwIJQcZnKSnS3Ccc20gvZ1bdrB_8XLCQZqA/formResponse","https://docs.google.com/forms/d/e/1FAIpQLSfsh_exyYg3g8654o7Tkfpz2VWSgMLy9KJp2SFIc5Hslpvp3g/formResponse","https://docs.google.com/forms/d/e/1FAIpQLSdTXyiIIkh3vJjoJlz4H6de5h4mPRlg7QKQ-z4fHf1mo5iiBQ/formResponse","https://docs.google.com/forms/d/e/1FAIpQLSfRYVxB5j2mE1b_Tf0BVNl3fX8o_PMse5kO_XsPeMOU9Skp7A/formResponse","https://docs.google.com/forms/d/e/1FAIpQLScE9OJhFZNGyHt6ESiIidH9ap_FzBPtNkAMJpeLn3TZYneknw/formResponse","https://docs.google.com/forms/d/e/1FAIpQLSeT5IB0STSo4sdkGxoTQndwAfvRUiHwY9LzesQxxVRsCaWLTQ/formResponse","https://docs.google.com/forms/d/e/1FAIpQLScoI2XiNvEjC2FiCukhVEQgRpRftqkd0l6lrhkSJQ0QaBGv7g/formResponse","https://docs.google.com/forms/d/e/1FAIpQLSc8YEyLHwqy66NINGJ4QbG7alRfhsQAplvDbeP_sGbXuMc4DA/formResponse","https://docs.google.com/forms/d/e/1FAIpQLSdK4RPrwDD5nem7nhx3kSduqHkB6CY5ELM3uEDiPQEUqs5D7g/formResponse","https://docs.google.com/forms/d/e/1FAIpQLSdTJ6o-0nl88atYVkRkVjPiJdZL1awsfAVudQQtP7IXXZDQDg/formResponse"
] #insert your Google Form link here, replace '/viewform' by '/formResponse'

for i in range(0,10): # set number of responses you wish to send
    submission = {"entry.1404348575": "181910172",
                  "entry.1214830987": "HIDAYAT"
					} # get the entry id as explained in the README.md and fill the dictionary
    print(submission)
    try:
        requests.post(url[i], submission) # store the outcome of POST request	ient:
    except:
        print("error")
    # print(sent)
    # if sent:
    #     print('Success!')
    # else:
    #     print('maaf kamu gagal')
    