from api_testing.api.client import Client


class HttpBinApi(Client):
    HTML = "/html"
    BASE_URL = "https://httpbin.org"
    IMAGE_JPEG = "/image/jpeg"
    ROBOTS = "/robots.txt"

    def list_html(self):
        """
        :method:    get
        :routs:     /html
        :status:    200
        """
        url = self.BASE_URL + self.HTML
        return self.get(url)

    def image_jpeg(self):
        """
        :method:    get
        :routs:     /image/jpeg
        :status:    200
        """
        url = self.BASE_URL + self.IMAGE_JPEG
        return self.get(url)

    def robots_txt(self):
        """
        :method:    get
        :routs:     /robots.txt
        :status:    200
        """
        url = self.BASE_URL + self.ROBOTS
        return self.get(url)


http_bin_api = HttpBinApi()
