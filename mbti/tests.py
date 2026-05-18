from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from django.test import TestCase
from django.urls import reverse

from .models import MBTIType


class MBTITypeModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.infp = MBTIType.objects.create(
            name="INFP",
            description="Curious and reflective personality.",
            logic=65,
            imagination=90,
            discipline=45,
        )

    def test_str_returns_name(self):
        self.assertEqual(str(self.infp), "INFP")

    def test_name_is_unique(self):
        duplicate = MBTIType(
            name="INFP",
            description="Duplicate name",
            logic=50,
            imagination=50,
            discipline=50,
        )

        with self.assertRaises(ValidationError):
            duplicate.full_clean()

    def test_trait_validators_reject_values_outside_0_100(self):
        invalid = MBTIType(
            name="ENTJ",
            description="Invalid logic",
            logic=101,
            imagination=60,
            discipline=60,
        )

        with self.assertRaises(ValidationError):
            invalid.full_clean()

    def test_db_check_constraint_rejects_invalid_trait(self):
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                MBTIType.objects.create(
                    name="ENTP",
                    description="Invalid discipline",
                    logic=60,
                    imagination=60,
                    discipline=-1,
                )


class MBTIViewsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.infp = MBTIType.objects.create(
            name="INFP",
            description="Creative and idealistic.",
            logic=65,
            imagination=90,
            discipline=45,
        )
        cls.estj = MBTIType.objects.create(
            name="ESTJ",
            description="Organized and practical leader.",
            logic=85,
            imagination=45,
            discipline=95,
        )

    def test_home_page_renders(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/home.html")
        self.assertContains(response, "INFP")
        self.assertContains(response, "ESTJ")

    def test_home_page_search_filters_results(self):
        response = self.client.get(reverse("home"), {"q": "idealistic"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "INFP")
        self.assertNotContains(response, "ESTJ")
        self.assertEqual(response.context["q"], "idealistic")

    def test_mbti_detail_page_renders(self):
        response = self.client.get(reverse("mbti_detail", args=[self.infp.pk]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/mbti_detail.html")
        self.assertContains(response, "INFP")

    def test_mbti_detail_404_for_missing_item(self):
        response = self.client.get(reverse("mbti_detail", args=[9999]))
        self.assertEqual(response.status_code, 404)

    def test_about_page_renders(self):
        response = self.client.get(reverse("about"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/about.html")
