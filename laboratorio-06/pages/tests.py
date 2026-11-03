from django.test import TestCase
from django.urls import reverse


class ClassroomHubViewsTests(TestCase):
    def test_home_returns_200_and_uses_template(self):
        response = self.client.get(reverse("pages:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/home.html")
        self.assertContains(response, "ClassroomHub")

    def test_resources_returns_200_and_shows_available_and_pending_states(self):
        response = self.client.get(reverse("pages:resources"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/resources.html")
        self.assertContains(response, "Disponible")
        self.assertContains(response, "Próximamente")

    def test_about_returns_200_and_uses_shared_template(self):
        response = self.client.get(reverse("pages:about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/about.html")
        self.assertContains(response, "Tecnologías")

    def test_navigation_uses_named_routes(self):
        response = self.client.get(reverse("pages:home"))
        self.assertContains(response, reverse("pages:resources"))
        self.assertContains(response, reverse("pages:about"))

    def test_unknown_url_returns_404(self):
        response = self.client.get("/ruta-inexistente/")
        self.assertEqual(response.status_code, 404)
