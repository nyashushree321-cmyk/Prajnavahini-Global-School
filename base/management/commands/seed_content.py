from pathlib import Path

from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand

from base.models import (
    AfterSchoolProgram,
    BlogPost,
    CampusFacility,
    CurricularProgram,
    FAQItem,
    InfraFeature,
    LeaderMessage,
    Mentor,
    OngoingClass,
)

STATIC_IMG = Path(settings.BASE_DIR) / 'static' / 'img'


def attach_image(instance, field_name, relative_path):
    src = STATIC_IMG / relative_path
    if not src.exists():
        raise FileNotFoundError(src)
    with src.open('rb') as f:
        getattr(instance, field_name).save(src.name, File(f), save=False)


class Command(BaseCommand):
    help = "Seed the database with the original site's copy so the pages are not blank on first run."

    def handle(self, *args, **options):
        self.seed_infra_features()
        self.seed_leader_messages()
        self.seed_mentors()
        self.seed_after_school_programs()
        self.seed_campus_facilities()
        self.seed_curricular_programs()
        self.seed_ongoing_classes()
        self.seed_blog_posts()
        self.seed_faq_items()
        self.stdout.write(self.style.SUCCESS('Content seeded.'))

    def seed_infra_features(self):
        if InfraFeature.objects.exists():
            return
        data = [
            ('Child-Safe Environment', '#ff7350', 'infra/Child-Safe Environment.png',
             'Furniture, flooring, and play equipment are designed with child safety as the top priority to ensure comfort and security.'),
            ('Age-Appropriate Learning Zones', '#021341', 'infra/Age-Appropriate Learning Zones.png',
             'Separate, well-planned spaces for Toddlers, Nursery, and Kindergarten, designed for exploration and engagement.'),
            ('Safety & Security', '#125875', 'infra/Safety & Security.png',
             'CCTV surveillance in classrooms and corridors, trained security staff, and regular safety drills for student well-being.'),
            ('Hygiene & Health', '#ff7350', 'infra/Hygiene & Health.png',
             'A hygienic kitchen, clean restrooms with attendants, and a medical aid room with trained staff ensure care at every step.'),
            ('Modern Classrooms', '#021341', 'infra/Modern Classrooms.png',
             'Bright, airy, and technologically integrated classrooms equipped with child-friendly teaching aids to enhance learning.'),
            ('Outdoor & Play Facilities', '#125875', 'infra/Outdoor & Play Facilities.png',
             'A spacious playground designed for physical fitness, teamwork, and joyful learning through play.'),
        ]
        for order, (title, color, img, desc) in enumerate(data, start=1):
            obj = InfraFeature(title=title, background_color=color, description=desc, order=order)
            attach_image(obj, 'image', img)
            obj.save()

    def seed_leader_messages(self):
        if LeaderMessage.objects.exists():
            return
        konnur_bio = (
            "It is with great joy that I welcome you to Prajnavahini Global School — a nurturing space "
            "where young minds are guided to explore, express, and excel. With decades of experience in academia, "
            "having served in key positions at universities such as Goa University, Bangalore University, and Rani "
            "Channamma University, I am honoured to lead this institution into a future of meaningful and purposeful "
            "holistic education.\n\n"
            "My continued work as President of LIS Academy has strengthened my belief in the transformative power of "
            "learning — a vision we bring to life at Prajnavahini. Situated in Sir M. Visvesvaraya Layout, Bangalore, "
            "our school offers a strong early education foundation through pre-primary programs and is expanding to "
            "include Grades 1 to 5 under the globally recognized IGCSE curriculum.\n\n"
            "We are committed to creating a joyful, secure, and future-ready learning environment. I invite you to "
            "join us on this inspiring journey of nurturing tomorrow's leaders."
        )
        vidya_bio = (
            "Dear Parents and Guardians,\n\n"
            "Warm greetings from Prajnavahini Global School!\n\n"
            "Vidya S is an experienced academic leader and educator with over 19 years of expertise in teaching, "
            "educational administration, teacher training, and curriculum development. She has worked as a Teacher, "
            "Academic Head, Regional Trainer, and Coordinator across reputed institutions, specializing in Montessori "
            "methods, Cambridge-aligned literacy, phonics, inclusive education, and professional development programs. "
            "She has been honored with the National Excellence Achievers Award for her outstanding contribution as an "
            "\"Excellent Educationist.\"\n\n"
            "Welcome to Prajnavahini Global School, located in the heart of Sir M. Visvesvaraya Layout, Bangalore, "
            "where we are dedicated to nurturing young minds through joyful, future-focused education. Our Pre-Primary "
            "program is thoughtfully designed to create a safe, nurturing, and stimulating environment that encourages "
            "curiosity, creativity, and confidence in young learners.\n\n"
            "We believe that early childhood education lays the foundation for lifelong learning. Through "
            "Montessori-inspired practices, interactive activities, and holistic development programs, we focus on "
            "nurturing each child's social, emotional, intellectual, and physical growth.\n\n"
            "At Prajnavahini, we value the strong partnership between parents and educators in shaping a child's "
            "future. Together, we aim to create happy learners who grow into confident, compassionate, and "
            "responsible individuals.\n\n"
            "We warmly welcome you to be a part of our school family and look forward to a wonderful journey of "
            "learning and growth together."
        )
        data = [
            ('Prof. P.V. Konnur', 'Director, Prajnavahini Global School', 'team/ji5a5431-enhanced-nr-2-scaled.jpg', konnur_bio),
            ('Ms. Vidya S', 'Principal, Prajnavahini Global School', 'team/vidya.jpeg', vidya_bio),
        ]
        for order, (name, designation, img, bio) in enumerate(data, start=1):
            obj = LeaderMessage(name=name, designation=designation, bio=bio, order=order)
            attach_image(obj, 'photo', img)
            obj.save()

    def seed_mentors(self):
        if Mentor.objects.exists():
            return
        data = [
            (
                'Mrs. Pritam L. Benjamin',
                'Vice Principal, Bangalore International School\nNational Academy for Learning (NAFL),\nIndus '
                'International School, Inventure Academy,\nCurrently Advisor and Education Consultant ·\nIndus Trust '
                'and EVOLVED.IN',
                'team/ji5a5597-scaled.jpg',
                '"Holistic education nurtures not just the mind, but also the body and spirit, shaping confident, '
                "compassionate, and capable individuals. It's about shaping character, encouraging curiosity, and "
                'fostering empathy. By embracing this approach, we empower students to thrive in an everchanging '
                'world. At Prajnavahini Global School, we strive to create a nurturing environment that brings out '
                'the best in every child."',
            ),
            (
                'Dr. Meera Krishnappa',
                'Former Teacher –Coordinator\nNational Academy for Learning (NAFL),\nRajajinagar Bangalore\nFormer, '
                'Principal,\nDr. NSAM First Grade Degree College, Mangalore',
                'team/ji5a5618-scaled.jpg',
                '"True learning happens when education goes beyond textbooks — when it builds confidence, character, '
                'and creativity. At Prajnavahini Global School, we nurture minds that think beyond boundaries. '
                'Empowering students to shape a brighter future, one innovation at a time."',
            ),
            (
                'Ms. Eshwari K',
                'Former Teacher NPS\nHead Of Operations PGS',
                'team/screenshot (63).png',
                '"PGS stands out as a premier institution in the locality, offering world-class international '
                'education that nurtures young minds and empowers future leaders."',
            ),
            (
                'Ms. Roopa Ramakrishna',
                'Advisor Prajnavahini Global School',
                'team/screenshot (64).png',
                '"At PGS, our top priority is creating a safe, caring, and nurturing environment where every child '
                'can thrive, grow, and reach their full potential. We believe in fostering a culture of kindness, '
                'respect, and empathy, where every child feels valued and supported. Our school operates with '
                'transparency, integrity, and a commitment to excellence, ensuring every student receives a '
                'world-class education."',
            ),
        ]
        for order, (name, title, img, quote) in enumerate(data, start=1):
            obj = Mentor(name=name, title=title, quote=quote, order=order)
            attach_image(obj, 'photo', img)
            obj.save()

    def seed_after_school_programs(self):
        if AfterSchoolProgram.objects.exists():
            return
        data = [
            ('Abacus and Vedic Math', 'Programmes/Abacus and Vedic Math.jpg'),
            ('Robotics', 'Programmes/Robotics.jpg'),
            ('Day Care', 'Programmes/daycare.jpg'),
            ('Tutorials', 'Programmes/Basics of Computer for Homemakers.jpg'),
            ('Zumba, Yoga and Dance', 'Programmes/dance.jpg'),
        ]
        for order, (title, img) in enumerate(data, start=1):
            obj = AfterSchoolProgram(title=title, order=order)
            attach_image(obj, 'image', img)
            obj.save()

    def seed_campus_facilities(self):
        if CampusFacility.objects.exists():
            return
        data = [
            ('features/hero-img--1152x1536.jpg', 'Thoughtfully Designed Campus'),
            ('Innovation/childsafe.jpg', 'Child-Safe Furniture, Flooring & Play Equipment'),
            ('Innovation/Separate Age-Appropriate Zones.jpg', 'Age-Appropriate Zones (Toddlers, Nursery, Kindergarten)'),
            ('Innovation/Safety & Security.png', 'CCTV Surveillance in Classrooms & Common Areas'),
            ('Innovation/Regular Safety Drills & Trained Security Staff.png', 'Regular Safety Drills & Trained Security Staff'),
            ('infra/Hygiene & Health.png', 'Hygienic Kitchen & Clean Restrooms with Attendants'),
            ('infra/Outdoor & Play Facilities.png', 'Well-Equipped Playground'),
            ('Innovation/Child-Friendly Teaching Aid.jpg', 'Child-Friendly Teaching Aids'),
            ('Innovation/Provision for Daycare.jpg', 'Provision for Daycare'),
            ('Innovation/Bright & Airy Classrooms.jpg', 'Bright & Airy Classrooms'),
            ('Innovation/Advanced Technologically Integrated Classrooms.jpg', 'Advanced Technologically Integrated Classrooms'),
            ('Innovation/Medical Aid Room with Trained Staff.png', 'Medical Aid Room with Trained Staff'),
        ]
        for order, (img, caption) in enumerate(data, start=1):
            obj = CampusFacility(caption=caption, order=order)
            attach_image(obj, 'image', img)
            obj.save()

    def seed_curricular_programs(self):
        if CurricularProgram.objects.exists():
            return
        data = [
            ('Earlyyears', 'Age 3+', 'bg/bengaluru-early-years.webp',
             'A holistic curriculum\nEngaging resources\nSupport to measure progress'),
            ('Primary', 'Age 5+', 'bg/blog-24(new)-1024x574.jpg',
             'Clear,adaptable curriculum\nFlexible assessment options\nSupport and resources\nInsight to understand potential'),
        ]
        for order, (title, age_badge, img, features) in enumerate(data, start=1):
            obj = CurricularProgram(title=title, age_badge=age_badge, features=features, order=order)
            attach_image(obj, 'image', img)
            obj.save()

    def seed_ongoing_classes(self):
        if OngoingClass.objects.exists():
            return
        data = [
            ('Creative Arts', 'Drawing, Clay modeling, Craft', 'class/creativeart.jpg'),
            ('Music & Movement', 'Singing, Dancing, Yoga', 'class/music and movement.jpg'),
            ('Life Skills', 'Grooming,Gardening,Outdoor Exploration', 'class/240739-1600x1067-kids-gardening-1.webp'),
            ('Cultural Celebrations', 'Festivals, Themed Dress-up days', 'class/2017_8$largeimg12_saturday_2017_004213296.jpg'),
            ('Special Days', 'Sports Day,Storytelling Sessions.', 'class/dsc_7505-1600x1064.jpg'),
            ('Skill-Based Clubs', 'Vedic Math, Public Speaking, Robotics', 'class/class-6.jpg'),
        ]
        for order, (title, subtitle, img) in enumerate(data, start=1):
            obj = OngoingClass(title=title, subtitle=subtitle, order=order)
            attach_image(obj, 'image', img)
            obj.save()

    def seed_blog_posts(self):
        if BlogPost.objects.exists():
            return
        data = [
            (
                'Learning Beyond Books – The Prajnavahini Way',
                'blog/1.webp',
                "At Prajnavahini Global School, education isn't confined to textbooks or classrooms. We believe "
                'that true learning happens when students connect knowledge to the real world. Our innovative '
                'teaching methods focus on experiential learning, where children explore, question, and apply '
                'concepts through hands-on activities.',
            ),
            (
                'Global Education, Local Values',
                'blog/wcp-2309211307-1370611298.jpg',
                'At Prajnavahini Global School Our Integrated Pre-Primary Program is based on global methodologies '
                'that promote exploration, creativity, and independence. As we expand to offer Grades 1–5 under the '
                'Cambridge IGCSE curriculum, students will experience an academic framework that builds critical '
                'thinking, digital literacy, and a global perspective.',
            ),
            (
                'Building the Future – One Child at a Time',
                'blog/2.jpg',
                'At PGS, every child matters. We understand that each learner is unique, with their own strengths, '
                "interests, and pace. That's why our approach is personalized and nurturing, encouraging students to "
                'discover their potential through guided exploration and real-life experiences. We believe that '
                "education is not about preparing for exams — it's about preparing for life.",
            ),
        ]
        for order, (title, img, excerpt) in enumerate(data, start=1):
            obj = BlogPost(title=title, excerpt=excerpt, order=order)
            attach_image(obj, 'image', img)
            obj.save()

    def seed_faq_items(self):
        if FAQItem.objects.exists():
            return
        data = [
            (
                'What makes Prajnavahini Global School different from other schools?',
                'Prajnavahini Global School goes beyond traditional academics by combining classroom learning with '
                'real-life experiences. Our unique approach focuses on developing confident, compassionate, and '
                'capable individuals through experiential and holistic education',
            ),
            (
                'Where is Prajnavahini Global School located?',
                'The school is located at #9, 9th Block, Sir M. Visvesvaraya Layout, Bangalore, offering a serene '
                'and well-connected environment conducive to learning and growth',
            ),
            (
                'What programs does PGS currently offer?',
                'Our community is being called to reimagine the future. As the only university where a renowned '
                'design school comes together with premier colleges, we are making learning more relevant and '
                'transformational. We are enriched by the wide range.',
            ),
            (
                'Which curriculum will PGS follow for higher grades?',
                'Starting from the upcoming academic year, PGS will offer Grades 1 to 5 under the internationally '
                'recognized Cambridge IGCSE curriculum, which emphasizes analytical thinking, digital literacy, and '
                'a global outlook',
            ),
            (
                "What is the core philosophy of PGS's teaching approach?",
                'Our community is being called to reimagine the future. As the only university where a renowned '
                'design school comes together with premier colleges, we are making learning more relevant and '
                'transformational. We are enriched by the wide range.',
            ),
        ]
        for order, (question, answer) in enumerate(data, start=1):
            FAQItem.objects.create(question=question, answer=answer, order=order)
