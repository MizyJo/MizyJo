PGDMP     2    ;                |            vitrine_aro    14.5    14.5 (    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16457    vitrine_aro    DATABASE     l   CREATE DATABASE vitrine_aro WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_Madagascar.1252';
    DROP DATABASE vitrine_aro;
                postgres    false            �          0    16481 
   auth_group 
   TABLE DATA           .   COPY public.auth_group (id, name) FROM stdin;
    public          postgres    false    216   �#       �          0    16489    auth_group_permissions 
   TABLE DATA           M   COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
    public          postgres    false    218   ;$       �          0    16475    auth_permission 
   TABLE DATA           N   COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
    public          postgres    false    214   %       �          0    16495 	   auth_user 
   TABLE DATA           �   COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
    public          postgres    false    220   �'       �          0    16503    auth_user_groups 
   TABLE DATA           A   COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
    public          postgres    false    222   @+       �          0    16509    auth_user_user_permissions 
   TABLE DATA           P   COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
    public          postgres    false    224   v+       �          0    16567    django_admin_log 
   TABLE DATA           �   COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
    public          postgres    false    226   �+       �          0    16467    django_content_type 
   TABLE DATA           C   COPY public.django_content_type (id, app_label, model) FROM stdin;
    public          postgres    false    212   �-       �          0    16459    django_migrations 
   TABLE DATA           C   COPY public.django_migrations (id, app, name, applied) FROM stdin;
    public          postgres    false    210   m.       �          0    16595    django_session 
   TABLE DATA           P   COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
    public          postgres    false    227   �1       �          0    65644    vitrine_agence 
   TABLE DATA           ]   COPY public.vitrine_agence (id, nom, telephone, date, update_at, photo, adresse) FROM stdin;
    public          postgres    false    240   �7       �          0    41059    vitrine_apropos 
   TABLE DATA           d   COPY public.vitrine_apropos (id, titre, description, icone, date, is_active, update_at) FROM stdin;
    public          postgres    false    238   X8       �          0    24651    vitrine_article 
   TABLE DATA           h   COPY public.vitrine_article (id, titre, description, image_url, date, is_active, update_at) FROM stdin;
    public          postgres    false    229   �:       �          0    65652    vitrine_autre 
   TABLE DATA           r   COPY public.vitrine_autre (id, grand_titre, petit_titre, email, telephone, date, update_at, pourquoi) FROM stdin;
    public          postgres    false    242   �>       �          0    32866    vitrine_customuser 
   TABLE DATA           F   COPY public.vitrine_customuser (user_ptr_id, first_login) FROM stdin;
    public          postgres    false    236   �?       �          0    24659    vitrine_departement 
   TABLE DATA           j   COPY public.vitrine_departement (id, nom, description, image_url, date, is_active, update_at) FROM stdin;
    public          postgres    false    231   @       �          0    73836    vitrine_equipe 
   TABLE DATA           D   COPY public.vitrine_equipe (id, photo, date, update_at) FROM stdin;
    public          postgres    false    244   �B       �          0    24705    vitrine_prix 
   TABLE DATA           X   COPY public.vitrine_prix (id, nom, prix, icone, date, is_active, update_at) FROM stdin;
    public          postgres    false    235   cD       �          0    24667    vitrine_service 
   TABLE DATA           i   COPY public.vitrine_service (id, nom, description, icone, date, is_active, update_at, photo) FROM stdin;
    public          postgres    false    233   9E       �           0    0    auth_group_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.auth_group_id_seq', 50, true);
          public          postgres    false    215            �           0    0    auth_group_permissions_id_seq    SEQUENCE SET     M   SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 217, true);
          public          postgres    false    217            �           0    0    auth_permission_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.auth_permission_id_seq', 60, true);
          public          postgres    false    213            �           0    0    auth_user_groups_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 79, true);
          public          postgres    false    221            �           0    0    auth_user_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.auth_user_id_seq', 11, true);
          public          postgres    false    219            �           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 21, true);
          public          postgres    false    223            �           0    0    django_admin_log_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.django_admin_log_id_seq', 19, true);
          public          postgres    false    225            �           0    0    django_content_type_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.django_content_type_id_seq', 15, true);
          public          postgres    false    211            �           0    0    django_migrations_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.django_migrations_id_seq', 33, true);
          public          postgres    false    209            �           0    0    vitrine_agence_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.vitrine_agence_id_seq', 4, true);
          public          postgres    false    239            �           0    0    vitrine_apropos_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.vitrine_apropos_id_seq', 5, true);
          public          postgres    false    237            �           0    0    vitrine_article_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.vitrine_article_id_seq', 10, true);
          public          postgres    false    228            �           0    0    vitrine_autre_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.vitrine_autre_id_seq', 1, false);
          public          postgres    false    241            �           0    0    vitrine_departement_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.vitrine_departement_id_seq', 13, true);
          public          postgres    false    230            �           0    0    vitrine_equipe_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.vitrine_equipe_id_seq', 10, true);
          public          postgres    false    243            �           0    0    vitrine_prix_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.vitrine_prix_id_seq', 7, true);
          public          postgres    false    234            �           0    0    vitrine_service_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.vitrine_service_id_seq', 11, true);
          public          postgres    false    232            �   �   x�-�K�0D��a*҆~�R	Y� W@"�A�R�ы5vc�ͼ3|?�@��ft0�^	d�}����̋e�ARy��K��[Ȭ��]�ƒ��A1�$3��E��Ewz�b%�)V���+4�U��Xg�Y��4�R�mTL���	�'D���C�      �   4  x��a� ��ü
�]v�s��dI?���f��yp�'�VW���	$��U�I���dݺ�:��G�9���S�_z���b��l�Emi�L�(_��:To��z�Bj�\%�*�a�'}��2�^Lx&M<�ޑ>��l���DoA�MʵK}�}���mt�=�L�c�6�ubY�l�|��P�hv�6�κ�}Cڥ_��F1Μ��F]l�5�AH������(6�)�Δ��l�|(Hg(I���|�@�sMlg��L}5g�����Bλ�9�����7}M�jarvU�9�cr�/�� �ۼca      �   <  x�e�[n�0E��Ud�ʯ$߳��������}>D2�3�� �b���O��r9���!N[�v���#�P�
��_?]���H��K��͂x$`�c��{��%�����<�
���wZ΀d�أ�3,	*�$��Gŝ��5���j�o޴�ɋ���!B*Qa ,�]�}��5 ������S��G�շ@�#���Ԇ��y,7����%���y��I���$d���z��O�՛h�Рk�P�׈S�@�*_��C�3i��
��.XD�ާmn���*_��CF3���
��-DR}�K>����X�_��[��n�nq�4�J���֠��jz�Ctg�*T�n�T�)S%��Se�L��NO�!�*!�:�4~��`u�o_���m^X@����'Ѩ�s�t��
w����|���T��C(+]s���F�\�*-tͨ�/i^����T��F] �:s6��qؙ�a
�Ό����=y��8V�5!���2����R�u��$���r7:�51. � c2\AF���}Io���y�\�X��$XaʤX(R!�SId�x���$��      �   e  x�}Tko�\����~3�s�C��zÊJ�zA�&o��M�୿~�����.LfH8���yf��p��3_ �j���)�ı38�,f�i���\]�Z�?.��7��W�Ge��=w}�ƃ��昿ԭ���CB �@�B�!�&s� K�v(!�ޣ.b�N��ǿ�^$��l'Qq>ψ ����"i���c�qg��#tth��G��fMg�4j����6���.��a7K�$<-甌���(��h2�0d�(��C.�~༼\wI,r_Ē$�m�?o��w�G߀U��0�U q�<��yݚ��lΎ^o�u�� 7�eY�w��2���ZY��[��ۭ�p��7$j�֣�F;:�� �U#DL�J`�D����V!� �0��4��������So�;g��`~
�V6�-�xTO1x>���|=��i�L箮�Wv����f��O �B�� �L	/�7qr<9��]�G9�@+��#�2[�އ1���kwo�{8�E��L��k�A�K��Ƨ�Ջ̦4��޳��T\���V�X���Y���yQ�3�.�Ή�HH�[��$qR.����$a�d"�av��_��O�.�ϫK���4���ox��X�^Cݿ���=9�A��Y�7�C�;���%{�jD�UR��Il��*����c���QRd� �7��}�se�|7��^6|��4��p�[�`t��-s�1����Yx���ӗW��竳u�/� K�&��p,�n��Q��b�8@����웺���ԁ����~�uf�Zl�Nؙ��y�O��nS\쩳��v�+ܚ�����0��B��W���~��k���9Ŭ���\�T~R۴<      �   &   x�36�4�4�27�44�4��2��44�44����� D�F      �   N   x����0��x�&	��t�9j�t�b����1q
��/�����U`�'�|7�c9�ݷ�~�_��؉Jw"���)l      �   �  x���Mn�0���)m�3C�.�m�i�$�L-ې� @���X)�El���}����(H? = ���� -8��(����q��؜�>}?}e]7u����"���	EC@#[=RH���ٔ�B]!|��K�4{J�uw3j=U� V�5dsZ����R<%��^*��yJ��P�,w/#���f[���T<6]�>�w}��n�p %*e=���n���+��,����w_�&p��Ic�.`�7�[�����[ ���:� #��PvǦmv�9�Iz�xL��.�ϩ�V�V*$�\���Xmg������+(E-�#�ڴ�-����vkpԐiP���v,9�۟g32U_QS�(�S2 =nJ�_e�˗XZK�@�+tY�Yb��TK�h���C�W
����3 :�ċ��ǥMů8cMצ��dRP^�����#Q6���љ����1nc��������/�LZ      �   �   x�M�I�0е}D:0܅M�Z�R3`'�=�)��'��60��=�a"�d����I�r���2I��=d%�l���I�^@ik��WX8	{�Aۙ�Ve�X�\��j���%4�JQ����l���mLs�bP4�A��W�!9I���2��'D� �_T      �   (  x����n�:E�����A��o)@��Э�$��L��R��H�쥙�����2K;,����'�8?��7�	�W��L�A�R� *ˬF��/xj���BVLq-ET�Ss���\�h�Q"t�x�Bçm?����?��z=f h��@��d��,~�Ϯ�����/d�!�+<��_n὘��qCӷ�(j�ˈ��>tM���Mm��<ǒ���͇���Fu���D��(��֙>ھ��3
2��b3E�������؞h4�� ��dtͼD�=u�v�g�H�4& ����_���介�C8{���Rޛ�_�es:�6�1�������������8s��3��Rr#�L�y�-��J���w�u�:}�Ѫ-c�2�:�E�����YL�?\h�)������l+fS2���v��U���m�d�������:3S��9VZRt�v@V����HS���iB���G�?���c(�n��kfk�
H�F�|�=�MX��k]�� �)��j�mZ,�]�y��oY�5��SF� !/u�H:�i|%�3�*�J�,rf�rE�RwU*4���=���(��nE�C�	�
�[W�|���}�%��'h2LZQ0�T)�J���6����Ц�������ץ��/	��5öu�� �dҕsI�U.\���Z�J+���S����N��E{��aX(�!b=�����n9���<�����i��RL�mU�r����}�%M��76y9� �=~��|������ˁ�Y�q���g1�(FQ:�9�c�Q�����7�      �      x���Ǫ�J��9O��M���L�r�βe�B)�,=��ݷφK��i��&}���*ߣQ�uYd�=�h[��iLF�CB��C@����%t ���4m�V��߉����Q;����X���D'��/ 8���%� `@� ��Y��Ҫ�(�6���Plu�Ӳ�O�U'5Qh�t�˺^�Irdkt���*�H����B���&���U	~Uń �U�%f��Eh��:9�}����3�n����*M�������v��OC=�̻7	�����ܟ�ٮ�^tW�?�
c�cȽ���]k���0-k#��f~�	4oȯ1[���+��'O�hQ��־�� G�q)k�2q6mF���ʵ����>v��qn<�]�rqI-\MVa��=uQ�ji�~�������Ƽj���+�U�M9Һ^/�:�'�u~P�������L��"��A��cc�vW�X��c;�tQ\I��$�F?��5?�mՐ��r��(-��)�yg�vHH����D��!c��)O^FET�ɪ �\/m�~�'i0ױ>���˚4q�Iy���q���j9�9"=]�R��BH�nˑ���m�F��2����y$b��F��u��2s �ݗB��gy�ФU����@�w��k�b�H-��4�s�óͦ���6f�?F����y	F�"�^F��:z���'������m.�t,P�?�ȿw��#7�]co���<=�]�S�ތ��}s�'�i+~��#H^F���	���]c�Y+tf�3h��?�$�5uX���g�(Xɲ���s�Z���Q7�zm�	J����;{�+�c�qJ��cĿ��p��<'���lSd'Y��$a[���@���;4�H�(�Rb�V��1���B��i�����"���h[z�ԯ���^D Id��~��N�~׵:l�"k�<k�����#�b���4�D���DWt���𼜪�u�+m3̵����d9s~���%�K�c
ze��8�*ɹ���!���P��('�g�I"=��>���m��q�?�ɍȅɺ�����2�U�?F�v���M����Q���!|����1�P۔�]U6_�ER|��ު�T��c�zwY�>,L���U�����(!zns��0���O;�G$<���CJ }!`Q�@��y�pv֦m�[z�[%6���Q��D��hy�ɘA�hK�f"�x_gk��FL�O�|�*?9�8�Z�	7� ���5Gt������T�����d��m)|�Q�����.-��L���7��Yf��hp#�Mj�Rk!OJ�ӳ��?��C�^!=�>g�uQ��eu�^q�cH���H߳�w�R4���a�ت�z�N��nb����23R��쨝�@��7s̋Y03"G߸U;�+a������|��Z����|��GpA�:�e}�����I�.��cy���1o�t�Ln�t�+��<X����Qwr1��Л�s��ʳ^�l�8x?�D��S��U���4����2��;QiV�U<�ڦ�Yќ��El��e��U��p�-�ѿǿ����N�      �   �   x�U�A�@Fϻ�b��3�k�M(��t� FYDб$/���N����𜪺(m�J�,��7��<Y �~=E�\j]��t�3���2�ٟ-CN�A[��6�k짙�����|;-/�N]�1.Ͱ��i���^�7ӰNXߍ��E�-�      �   4  x��S;r�0��Sl�"�A�f�I��=��,ɕ��h�#�)�&��Ų c��|fRq����o�D�%�ǡ�z������;�C�q� ���9�Xt�:7�ѩ�[G9~w��Է=��-�wxrGNr~����=��'���s�H!�g$�4�D[�{7�3jO�<�sFz�:L`֙>��y<��_P��<kOОVmTm�.�bU�U��r�E#6yY�ۛ�CQe����:�����Ւtpd���>�NV�q,�C+��xY�}Hk䰽�Õ�$�Nv�f��c�7b_�4��(�p�0]X��{�����H�K�<ړ�<J�����9�{�ف)C�ڃ��t$e����:/�U|%5��Gt�P֍��r!��Z�v�u�e#�\�E��*�o�ƁI�|�]���R�G��0�=�x��iZ%=���}���Ӻ��_�*py :Y�ٔ>��dK�ءt�����/gY��f�sҥ(i�)��E=3J�YEc��+�<R�YH9�9�J�'���I�	��F�Kc+O/�^ٺ�D^ע�6Sv�7Ey=��K�X,~4In�      �   A  x��U�nG����v#	����Yu�J�H�@1E�%9$�ڝaf����M� �G��R�M� M
wB~D?}B��J���I˽�3�>&ndgg_���A��^8Em�D�9t'1<�1��H-��~��^O���J*�9���F62|����}�Q�@������PH�#׿�	�q��uDR-KX����H4K]# �!8���G�i��S������n���v�z��{	�K�k�w�%psRp]��p�BC�g82K̅�ς4a�En4H�8	�(�R?rC��Q����4�\���7�{�ŴA�B��/j�����#������=r����l�F��y����^B�8�z�~/k�[Ъ�����*�B�m��	�b*:)H�RD�J!ʩ��۫��B���ㆬ���$�O���sy��;8���cN���b��K�m���T�a�::ph=peyD�)E��+��{�T�U�O�FT����fc�+�&�/x1T�yg��\R�Fʈ�
]�>*N���D�7`^�Fi�Q�,�R�1c��&i��~�~|q�F?�8��ɧ��V��2��k�.�}�H����k[�s:%�p�`� W+ҙ�d���(��p�3Q�1�
�ŏaN,�^�Ai8��.�tl�F����*.���%�녳P�AM�3�NO�@�
�΅Eac��m���};��
n5W���=�P�ܦ�k�m����n��ɚ�c�F�z0Ӣ4e�u��|&�\�<���V\K^������n���;-��K�P�Jۄ�:Vu���F�
�X�ZYI+Ke%���p�Ԥ�$��tHq?�tH)Q&�4, ��j����p{��r{��Oxz���}�A�l�1w�D��j�+�mߟR����W/�\��ԯs�4MB/I�h�,e�g���$��0
�+�`�&�L��" ^}f����u��'�.���@Zږ�8���^!&nj�L�}�ϸ-*�4�yW{VH�+x�n^��YM�Z��dw���%-t�\m����4�3*��/J(��s�4JX���������;b�IC��N�G�f�cQ2HRF[�Hs�����I��8����K9t<�<��mmm�M�q�      �   �   x��P=o�@��Wx���TU�FCC�P�.֝KO��CM��w��zT��N��%��~�2���)���myj������S�MՖ��h��:zAp�
f�-�u ^� �$���p���H�ѡpht:t�6���X�QƲbǊρ���"��{�g[�������	��2�"C���wxD�Z�&���I[?t8BS�|8Z7-�r�_	|�b�旛Sn-�%�dfE�ht���c�����9�����p�      �      x������ � �      �   �  x����r�0�k�)Թ����8]f������kd�8���9�Q���b��2̄��������}GU��d�Va�of�8KQ�U3m�]�R� ��fԮ]���i
0� i
5,g���R(�2�Q�]z�Y��YD�m����,�>��c-����i����e��כ���է�%9MY����4��H_F�e�j��'�a\_m�D�\�<���U5jw���B~���?�ܔO6E�~�»8���ЯR-�J4�q���	� %�W�~��Vq�������k�z(�׶�%$L���`��#�,|�-l�i�5m��Ƣ�B#�.�)�.�r���=["� (�xRy/\8�nM�}u��Qqq%ץ} � 8�m���"�q�9O�@ֹ� U�>���ָ�h��w��5ii��E�*��5��>�}�<���~ΠʓZ�B^�> i4��������]]I��������;P)�ܷ��>ߡp"���p��(�p�FY����нR�&؆�Uh5�Z�V9�6�(���$�����c�7Q�^��i��s�՚�7�D^>�Y!��CG:� <l��$�@%�9Ӎ��JZ|j�!V�i�<p�~SW�pg�ĽG{
߯�E�T�3��Y���}�}�c�����ط��]L_$��^�NU+O���m% �s�O��������Y����o�      �   y  x����j�A�k�S�����wƤ5�nc��L^ߣ��_�*E���3gh�������GaT!�!������4<�P����\$|����yC@�١nQ��+G~ ������If���d���n���bQ���5�f���V�����T�)����>&F0#A7MV�9XɎ`�w�T�����n2�Vjq|�@+T��~�e��k[�|!�\�/�3���
Z�}�� ����2ˁU=��*m�4Z�{ͦ���j��b���f(�Yk	��Hd���u�v��3����j��QW�u֣2!f����5��A42BBCq�Ƿ/�o~=_ �,J�PWN�X���?�{��~�x{7u�u�R�����zk�9w�      �   �   x���1�0�9����$@�V���bh�HPb*�H���5�B�x��e=�3rwn��;���*TF���!=���l4�$�2�Q��2���`�`��W&��ü�>lD��+-k������Bc��Ia�"�m>0HR��:����$e���ՔǮ���,ύmKk�<C�U���f1���:��J(�[��3�v�H�'I��#�{      �   �  x���Kn�0@��)��*R�c{�AQ$��*@�Pc�E*��MN�et]�C�Sg� ^�Da4�͌����˵ �qq��~te���Ƒ�[�溒F{D��J�p��4`=�q_����LW\{|5����ђ;�䉷A<�X��$�V�l��lQ���SV�Y>��H�"���rQ�l�f�	�M��J�S�u�[�u"�V6^��:��qb�WRC������M������X]���M��Y���yB����<��c���� ���Tp���p�K����-�i���r��k������=X������x��\b5�����?��KԤ�b6+�{������!���SZ���~;������kq��a[���K��[J!Qn5��	-�R@C[N��g�ivҠ��&z\�� {����O��i^eyL�
V��k1�|��ͽT���-N�wk)��!�������j�'66�\p��bo�.�t��4;�0~}J/�jz8L6w�&8+Z�M��!�ȅ&��W���_\zg�t�v�����߲з��ed���Y���0����u��&+�w�k�/��]y�%�W�T.��@{�zY7�n��kS�{K].�2e%e9;"�ͭ�1?�>�ߥ����G     