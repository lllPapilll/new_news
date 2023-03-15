init -1:
    # Ручка дверi вулиця
    transform r2_c:
        xalign 0.903 yalign 0.68
    transform r2_s:
        xalign 0.0 yalign 1.0
    transform r2_k:
        xalign 1.0 yalign 0.7

init -1: # art
    transform light_an:
        alpha 1.0
        ease 2 alpha 0.6
        ease 8 alpha 1.0
        repeat
    transform map_zoom_butt1_alpha:
        alpha 0.5
    transform map_zoom_butt1_alpha1:
        zoom 0.95 alpha 0.9
        ease 0.5 alpha 0.5
    transform map_zoom_butt1:
        alpha 0.5
        on idle:
            ease 0.2 zoom 1.0 alpha 1.0
        on hover:
            ease 0.1 zoom 0.9
            ease 0.2 zoom 0.95 alpha 0.9
    transform sp_mini:
        zoom 2.7 xpos -1.1 ypos -0.45
        block:
            alpha 0.9
            ease 2 alpha 0.7
            ease 2 alpha 0.9
            repeat
    transform sp_mini1:
        zoom 2.7 xpos -1.1 ypos -0.45
        ease 0.15 ypos -0.48
        ease 0.15 ypos -0.45
        block:
            alpha 0.9
            ease 2 alpha 0.7
            ease 2 alpha 0.9
            repeat

    transform zoom_bit:
        ease 0.2 zoom 1.7 xpos -0.4 ypos -0.2
        #ease 0.5 zoom 1.3 xpos -0.2 ypos -0.2
        ease 0.5 zoom 1.0 xpos 0.0 ypos 0.0
    transform zoom_2:
        zoom 1
        linear 1.0 zoom 1.1 xpos -0.05 ypos -0.08
    transform alpha_menu:
        alpha 0 ypos 0.5 zoom 0.95
        ease 0.3 pass
        ease 0.3 alpha 1 ypos 0.75 zoom 1.0
        ease 0.2 ypos 0.7
        on idle:
            ease 0.1 zoom 1.0 alpha 0.95
        on hover:
            ease 0.1 zoom 1.05 alpha 1
            ease 0.5 alpha 0.9
            ease 0.3 alpha 1
            repeat

    transform nee:
        xalign 1.0 ypos -0.3 zoom 0.9
        linear 600 xalign 0.0
        linear 600 xalign 1.0
        repeat

    # light
    transform trl1:
        alpha 0 xpos -0.05
        ease 4 alpha 0.3 xpos -0.17
        ease 7 alpha 0.5 xpos 0.03
        ease 4 alpha 0.0 xpos -0.24
        ease 4 pass
        repeat
    transform trl2:
        alpha 0 xpos 0.02
        ease 4 alpha 0.7 xpos 0.0
        ease 6 alpha 0.4 xpos -0.17
        ease 4 alpha 0.0 xpos -0.0
        repeat
    transform trl3:
        alpha 0 xpos -0.05
        ease 4 pass
        ease 4 alpha 0.7 xpos 0.03
        ease 5 alpha 0.4 xpos -0.17
        ease 4 alpha 0.0 xpos -0.0
        repeat

    transform t_art0:
        ease 0.3 zoom 1.3 xpos -0.05 ypos -0.15
    transform t_art01:
        ease 1 zoom 1.4 xpos -0.13 ypos -0.11
    transform t_art02:
        zoom 1.4 xpos -0.13 ypos -0.11
        ease 1 zoom 1.7 xpos -0.25 ypos -0.14
    transform t_art1:
        ease 1 zoom 1.2 xpos -0.14 ypos -0.12
        ease 1 zoom 1.18
    transform t_art2:
        zoom 1.18 xpos -0.14 ypos -0.12
        ease 1 zoom 1.18 xpos -0.1 ypos -0.1
        ease 1 zoom 1.2
    transform t_art3:
        zoom 1.2 xpos -0.1 ypos -0.1
        ease 1 zoom 1.2 xpos -0.14 ypos -0.12
        ease 1 zoom 1.0 xpos 0.0 ypos 0.0
    transform zoom_1:
        ease 1 zoom 1.1 xpos -0.05 ypos -0.05
    transform zoom_0:
        zoom 1.1 xpos -0.05 ypos -0.05
        ease 1 zoom 1.0 xpos 0.0 ypos 0.0
    transform zoom_ekz:
        zoom 2.5 xpos -0.75 ypos -1.2
        ease 2.2 zoom 2.5 ypos -0.7
    transform zoom_ekz1:
        zoom 2.5 ypos -0.7 xpos -0.75
        ease 0.4 ypos 0.0 xpos 0.0 zoom 1.0
    transform zoom_ekz2:
        ypos 0.0 xpos 0.0 zoom 1.0
        ease 0.5 ypos -0.3 xpos -0.5 zoom 2.0
        ease 0.3 ypos -0.3 xpos -0.45 zoom 1.9
        ease 0.4 ypos -0.3 xpos -0.6 zoom 2.1
        ease 0.2 ypos 0.0 xpos -0.1 zoom 1.1
        ease 0.4 pass
        ease 0.3 ypos -0.1 xpos -0.1 zoom 1.1
        ease 0.7 ypos 0.0 xpos -0.1 zoom 1.1
        ease 1 pass
        ease 3 zoom 2.5 xpos -0.75  ypos -0.7
    transform ekz_att:
        ease 0.5 pass
        ease 0.3 zoom 1.01
        ease 0.3 zoom 1.0
    transform ekz_alpha:
        alpha 0.0
        ease 2 alpha 1.0
    transform alpha_ydar:
        alpha 0.0
        ease 0.4 pass
        ease 0.1 alpha 1.0
        ease 0.3 alpha 0.0
    transform pc_alpha:
        zoom 10 alpha 0.08 ypos -1.0
    transform pc_alpha1:
        alpha 0.09

    transform batton1_dia:
        ypos 0.23 alpha 0.0
        ease 0.1 ypos 0.15 alpha 1.0
        ease 0.2 ypos 0.2
        on hover:
            ease 0.1 alpha 0.6
        on idle:
            ease 0.3 alpha 1
    transform batton1_dia1:
        ypos 0.13 alpha 0.0
        ease 0.1 ypos 0.15 alpha 1.0
        ease 0.2 ypos 0.1
        on hover:
            ease 0.1 alpha 0.6 zoom 0.9
        on idle:
            ease 0.3 alpha 1 zoom 1.0





init -1: # Дівчинка
    transform m_no:
        alpha 0 xpos 0.55 ypos 0.15 zoom 1.5
        ease 0.2 alpha 1 ypos 0.16
        block:
            xpos 0.55 ypos 0.16 zoom 1.5
            ease 1.6 ypos 0.17 alpha 0.8
            ease 1.6 ypos 0.16 alpha 1
            repeat
    transform m_no1:
        ease 1.6 ypos 0.17 alpha 0.8
        ease 1.6 ypos 0.16 alpha 1
        repeat
    transform m_hide:
        ease 0.3 ypos 0.15 alpha 0.0
        repeat
    transform m_fig:
        alpha 0 xpos 0.55 ypos 0.15 zoom 1.5
        ease 0.2 alpha 1 ypos 0.16
        block:
            xpos 0.55 ypos 0.16 zoom 1.5
            ease 0.1 xpos 0.545 alpha 0.8
            ease 0.15 xpos 0.555 alpha 1
            ease 0.1 xpos 0.55 ypos 0.16 zoom 1.5
            ease 2 pass
            repeat
    transform m_fig1:
        ease 0.1 alpha 1 xpos 0.3 ypos 0.1 zoom 3.5
        ease 0.3 alpha 1 xpos 0.3 ypos 0.1 zoom 3.3











init -1:
    transform et_tr:
        xalign 0.022 yalign 0.15 alpha 1.0
        ease 0.2 pass
        ease 0.2 zoom 1.1
        ease 0.1 zoom 1.0
    transform et_tr1:
        xalign 0.022 yalign 0.15 alpha 1.0 zoom 1.0
        ease 0.4 zoom 1.1 xalign 0.02 yalign 0.145
        ease 0.2 zoom 1.0 xalign 0.022 yalign 0.15
        repeat
    transform dev_1:
        alpha 0 xalign 0.727 yalign 0.867
        ease 0.3 alpha 0.9
        block:
            linear 3 alpha 0.7
            linear 2 alpha 0.9
            repeat
    transform dev_2:
        alpha 0 xalign 0.205 yalign 0.727 zoom 1.1
        ease 0.3 alpha 0.9
        block:
            linear 3 alpha 0.7
            linear 2 alpha 0.9
            repeat
    transform dev_3:
        alpha 0 xalign 0.95 yalign 1.0
        ease 0.3 alpha 0.9
        block:
            linear 3 alpha 0.7
            linear 2 alpha 0.9
            repeat

    transform t_day1:
        alpha 0 xalign 0.5 yalign 0.5 zoom 2
        ease 0.5 alpha 1
        ease 1 pass
        ease 0.3 alpha 0
    transform t_day:
        alpha 0 xalign 0.5 yalign 0.5
        ease 0.3 alpha 1
        ease 1 pass
        ease 0.5 alpha 0
    transform os_menu_1:
        alpha 0 yalign 0.27 xpos 0.03
        ease 0.3 pass
        ease 0.3 yalign 0.17 alpha 1
    transform os_menu_11:
        alpha 0 yalign 0.3 xpos 0.03
        ease 0.3 pass
        ease 0.3 yalign 0.2 alpha 1
    transform os_menu_2:
        alpha 0 yalign 0.5 xpos 0.03
        ease 0.25 pass
        ease 0.3 yalign 0.4 alpha 1
    transform os_menu_22:
        alpha 0 yalign 0.4 xpos 0.03
        ease 0.25 pass
        ease 0.3 yalign 0.3 alpha 1
    transform os_menu_3:
        alpha 0 yalign 0.76 xpos 0.03
        ease 0.2 pass
        ease 0.3 yalign 0.66 alpha 1
    transform os_menu_33:
        alpha 0 yalign 0.7 xpos 0.03
        ease 0.2 pass
        ease 0.3 yalign 0.6 alpha 1
    transform os_menu_4:
        alpha 0 yalign 0.7 xpos 0.03
        ease 0.15 pass
        ease 0.3 yalign 0.6 alpha 1
    transform os_menu_5:
        alpha 0 yalign 0.8 xpos 0.03
        ease 0.1 pass
        ease 0.3 yalign 0.7 alpha 1
    transform os_menu_5:
        alpha 0 yalign 0.8 xpos 0.03
        ease 0.1 pass
        ease 0.3 yalign 0.7 alpha 1
    transform os_menu_6:
        alpha 0 yalign 0.9 xpos 0.03
        ease 0.05 pass
        ease 0.3 yalign 0.8 alpha 1
    transform os_menu_66:
        alpha 0 yalign 0.8 xpos 0.03
        ease 0.05 pass
        ease 0.3 yalign 0.7 alpha 1
    transform os_menu_7:
        alpha 0 yalign 1.0 xpos 0.03
        ease 0.3 yalign 0.95 alpha 1
    transform os_menu_77:
        alpha 0 yalign 1.1 xpos 0.03
        ease 0.3 yalign 1.0 alpha 1
    transform os_menu_777:
        alpha 0 yalign 0.85 xpos 0.03
        ease 0.3 yalign 1.0 alpha 1

    transform tr_clock:
        xpos 0.65 ypos 0.3
        # linear 60 rotate 90
    transform tr_clock1:
        xpos 0.22 ypos 0.564
    transform an_pereh_loc:
        ypos -0.135 xalign 0.0 alpha 1
        linear 1 xalign 0.003 alpha 0
    transform an_pereh_loc1:
        alpha 1
        linear 1 pass
        ease 0.0001 alpha 0
    transform an_pereh_loc2:
        alpha 0
        linear 1 pass
        ease 0.0001 alpha 1
    transform transient:
        ease 0.2 alpha 0.5
        ease 0.5 pass
        ease 0.3 alpha 1
    transform tran_xn:
        yalign 0.84 xalign 0.5
    transform ex_butt:
        on idle:
            ease 0.1 alpha 1.0 zoom 1.0
        on hover:
            ease 0.1 alpha 0.95 zoom 0.995
    transform start_butt:
        on idle:
            ease 0.1 alpha 1.0 zoom 1.0
        on hover:
            ease 0.1 alpha 0.5 zoom 0.95

    transform bad_butt:
        alpha 0.2 xalign 0.368 yalign 0.823
        on idle:
            ease 0.1 alpha 0.2
        on hover:
            ease 0.1 alpha 1.0
    transform pc_butt:
        alpha 0.0
        on idle:
            ease 0.3 alpha 0.0
        on hover:
            ease 0.3 alpha 1.0
    transform tr1_l1:
        alpha 0.0
        on idle:
            ease 0.3 alpha 0.0
        on hover:
            ease 0.3 alpha .5
    transform tr1_l0:
        alpha 0.0
        on idle:
            ease 0.3 alpha 0.0
        on hover:
            ease 0.3 alpha 0.0
    transform tr1_alpha:
        alpha 0
        ease 0.1 alpha 0.5
    transform an_clean:
        alpha 0.0 xalign 0.020 yalign 0.15
        ease 1 pass
        ease 0.2 alpha 1 xalign 0.025
    transform tv_eff:
        alpha 1
        ease 0.05 alpha 0.9
        ease 0.05 alpha 0.95
        ease 0.05 alpha 0.9
        ease 0.05 alpha 1
        ease 1 pass
        repeat

    transform m_in:
        xalign 0.5 ypos -1.5
    transform cgp_an:
        ypos -0.135 xalign 0.0
        linear 200 xalign 1.0
        linear 200 xalign 0.0
        repeat
    transform cgs_an:
        yalign 0.36 xalign 0.55 zoom 0.8

    transform mu_os:
        alpha 0.0 yalign 0.0 zoom 0.9
        ease 0.3 alpha 1.0 zoom 1.15
        ease 0.1 zoom 1.1
        on hide:
            ease 0.3 zoom 1.0 alpha 0
    transform mu_bu1:
        yalign 0.1 alpha 1 zoom 0.6
        ease 0.3 zoom 1.1

        # on selected_idle:
        #     ease 0.2 yalign 0.718
        on hover:
            ease 0.2 zoom 1.0 # akt
        on idle:
            ease 0.2 zoom 1.1
        on hide:
            ease 0.3 zoom 0.6 alpha 0
    transform mu_bu11:
        yalign 0.105 alpha 1 zoom 0.6
        ease 0.3 zoom 1.1

        # on selected_idle:
        #     ease 0.2 yalign 0.718
        on hover:
            ease 0.2 zoom 1.0 # akt
        on idle:
            ease 0.2 zoom 1.1
        # on show:
        #     yalign 0.83 alpha 0
        #     ease 0.3 yalign 0.709 alpha 1
        #     on selected_idle:
        #         ease 0.2 yalign 0.718
        #     on hover:
        #         ease 0.2 yalign 0.715
        #     on idle:
        #         ease 0.2 yalign 0.709
        on hide:
            ease 0.3 zoom 0.6 alpha 0

    # transform mu_bu0:
    #     yalign 0.83 alpha 0 zoom 1.1
    #     ease 0.3 yalign 0.71 alpha 1
    #     on selected_idle:
    #         ease 0.2 yalign 0.718
    #     on hover:
    #         ease 0.2 yalign 0.715
    #     on idle:
    #         ease 0.2 yalign 0.71
    #     # on show:
    #     #     yalign 0.83 alpha 0
    #     #     ease 0.3 yalign 0.71 alpha 1
    #     #     on selected_idle:
    #     #         ease 0.2 yalign 0.718
    #     #     on hover:
    #     #         ease 0.2 yalign 0.715
    #     #     on idle:
    #     #         ease 0.2 yalign 0.71
    #     on hide:
    #         ease 0.3 yalign 0.83 alpha 0
    transform mu_bu:
        yalign 0.027 alpha 1
        ease 0.3 zoom 1.1

        on hover:
            ease 0.2 zoom 1.07 # akt
        on idle:
            ease 0.2 zoom 1.1
        # on show:
        #     yalign 0.83 alpha 0
        #     ease 0.3 yalign 0.71 alpha 1
        #     on hover:
        #         ease 0.2 yalign 0.715
        #     on idle:
        #         ease 0.2 yalign 0.71
        on hide:
            ease 0.3 alpha 0


    transform mu_kk:
        xalign 0.705 yalign 0.94 rotate 0 alpha 1
        on show:
            xalign 0.705 yalign 1.1 alpha 0
            ease 0.3 xalign 0.705 yalign 0.94 rotate 0 alpha 1
        on hide:
            ease 0.3 xalign 0.705 yalign 1.07 alpha 0
    transform mu_k:
        xalign 0.705 yalign 1.1 alpha 0
        xalign 0.705 yalign 0.94 rotate 0 alpha 1
        block:
            linear 20 rotate 1360
            linear 20 rotate 0
            repeat
        # on hide:
        #     ease 5.5 xalign 0.705 yalign 1.07 alpha 0
    transform mu_kk1: # Не пра
        xalign 0.7746 yalign 0.94 alpha 1 rotate 0
        on show:
            xalign 0.7746 yalign 1.1 alpha 0 rotate 0
            ease 0.3 xalign 0.7746 yalign 0.94 alpha 1
        on hide:
            ease 0.3 xalign 0.7746 yalign 1.06 alpha 0
    transform mu_k1: # пра
        xalign 0.7746 yalign 0.94 alpha 0
        xalign 0.7746 yalign 0.94 alpha 1
        block:
            linear 20 rotate 1360
            linear 20 xalign 0.7746 yalign 0.94 rotate 0
            repeat
        # on hide:
        #     ease 0.5 xalign 0.7746 yalign 1.1 alpha 0

    transform mu_ona:
        xalign 0.819 yalign 0.768 alpha 0
        ease 0.5 pass
        ease 0.2 xalign 0.819 yalign 0.768 alpha 1
    transform mu_offa:
        xalign 0.804 yalign 0.768 alpha 0
        ease 0.5 pass
        ease 0.2 xalign 0.804 yalign 0.768 alpha 1


    transform zoom_bar_im:
        alpha 1.0
        ease 0.6 alpha 0.8
        ease 0.6 alpha 1.0
        repeat
    transform work_an:
        yalign 0.585 alpha 0.0
        ease 0.3 alpha 1.0
        ease 0.3 alpha 0.8
        ease 0.3 alpha 1.0
    transform map_work_tr:
        xpos 0.22 ypos 0.32 alpha 0.0 zoom 0.8
        easein 0.1 xpos 0.22 alpha 0.0
        easein 0.2 xpos 0.2 alpha 1.0 zoom 0.9
        ease 2 pass
        ease 0.3 alpha 0.0
        on hide:
            easein 0.1 xpos 0.4 alpha 0.0 zoom 0.8
    transform map_work_tr1:
        xpos 0.4 ypos 0.4 alpha 0.0 zoom 0.8
        easein 0.1 xpos 0.4 alpha 0.0
        easein 0.2 xpos 0.43 alpha 1.0 zoom 0.9
        ease 2 pass
        ease 0.3 alpha 0.0
        on hide:
            easein 0.1 xpos 0.4 alpha 0.0 zoom 0.8
    transform map_shop_tr:
        xpos 0.71 ypos 0.45 alpha 0.0 zoom 0.8
        easein 0.1 xpos 0.77 alpha 0.0
        easein 0.2 xpos 0.76 alpha 1.0 zoom 0.9
        ease 2 pass
        ease 0.3 alpha 0.0
        on hide:
            easein 0.1 xpos 0.75 alpha 0.0 zoom 0.8

    transform met_ka_dun1:
        on show:
            alpha 0 xalign 0.5 ypos 0.03
            block:
                ease 1 ypos 0.06 alpha 1
                ease 1 ypos 0.03
                repeat
        on hide:
            easein 0.2 alpha 0 ypos 0.13

    transform map_box_hago1: # Goblin1
        xpos 0.35 ypos 0.32 alpha 0.0 zoom 0.8
        easein 0.1 xpos 0.35 alpha 0.0
        easein 0.2 xpos 0.36 alpha 1.0 zoom 0.9
        on hide:
            easein 0.1 xpos 0.35 alpha 0.0 zoom 0.8
    transform met_ka_hago1:
        on show:
            alpha 0 xalign 0.22 ypos 0.13
            block:
                ease 1 ypos 0.16 alpha 1
                ease 1 ypos 0.13
                repeat
        on hide:
            easein 0.2 alpha 0 ypos 0.13

    transform map_box_hago2: # Goblin2
        xpos 0.30 ypos 0.51 alpha 0.0 zoom 0.8
        easein 0.1 xpos 0.30 alpha 0.0
        easein 0.2 xpos 0.31 alpha 1.0 zoom 0.9
        on hide:
            easein 0.1 xpos 0.30 alpha 0.0 zoom 0.8
    transform met_ka_hago2:
        on show:
            alpha 0 xalign 0.19 ypos 0.32
            block:
                ease 1 ypos 0.35 alpha 1
                ease 1 ypos 0.32
                repeat
        on hide:
            easein 0.2 alpha 0 ypos 0.13

    transform map_box_huci1: # city
        xpos 0.91 ypos 0.2 alpha 0.0 zoom 0.8
        easein 0.1 xpos 0.91 alpha 0.0
        easein 0.2 xpos 0.92 alpha 1.0 zoom 0.9
        on hide:
            easein 0.1 xpos 0.91 alpha 0.0 zoom 0.8
    transform met_ka_huci1:
        on show:
            alpha 0 xalign 0.84 ypos 0.07
            block:
                ease 1 ypos 0.04 alpha 1
                ease 1 ypos 0.07
                repeat
        on hide:
            easein 0.2 alpha 0 ypos 0.4

    transform map_box_huci2: # farm
        xpos 0.91 ypos 0.58 alpha 0.0 zoom 0.8
        easein 0.1 xpos 0.91 alpha 0.0
        easein 0.2 xpos 0.92 alpha 1.0 zoom 0.9
        on hide:
            easein 0.1 xpos 0.91 alpha 0.0 zoom 0.8
    transform met_ka_huci2:
        on show:
            alpha 0 xalign 0.83 ypos 0.43
            block:
                ease 1 ypos 0.40 alpha 1
                ease 1 ypos 0.43
                repeat
        on hide:
            easein 0.2 alpha 0 ypos 0.4

    transform map_box_calo: # castle
        xpos 0.51 alpha 0.0 zoom 0.8
        easein 0.1 xpos 0.51 alpha 0.0
        easein 0.2 xpos 0.52 alpha 1.0 zoom 0.9
        on hide:
            easein 0.1 xpos 0.51 alpha 0.0 zoom 0.8
    transform met_ka_calo:
        on show:
            alpha 0 xalign 0.4 ypos 0.4
            block:
                ease 1 ypos 0.43 alpha 1
                ease 1 ypos 0.4
                repeat
        on hide:
            easein 0.2 alpha 0 ypos 0.4

    transform anim_bar:
        xpos 0.0 alpha 0
        ease 0.2 xpos 0.05 alpha 1
        ease 6.6 pass
        ease 0.2 xpos 0.0 alpha 0

    transform xr_an_bytt:
        on hover:
            ease 0.1 alpha 0.5
        on idle:
            ease 0.1 alpha 1.0
    transform m_diss:
        alpha 0.0
        easein 1 alpha 1.0

    transform an_slmenu:
        xpos 0.75 alpha 0.0
        easein 0.2 xpos 0.7 alpha 1.0

    transform an_slmenu_num:
        xpos 0.605 ypos 1.0 alpha 0
        ease 0.3 alpha 1 ypos 0.94
        ease 0.2 ypos 0.96




    # transform an_slmenu4:
    #     xpos 0.53 alpha 0.0
    #     easein 0.1 xpos 0.53 alpha 0.0
    #     easein 0.2 xpos 0.52 alpha 1.0
    #     block:
    #         on hover:
    #             easein 0.2 alpha 0.8
    #         on idle:
    #             easein 0.2 alpha 1.0
    #         on hide:
    #             xpos 0.52 alpha 1.0
    #             easein 0.05 xpos 0.53 alpha 0.0
    #             easein 0.1 xpos 0.53 alpha 0.0
    # transform an_slmenu41:
    #     xpos 0.5405 alpha 0.0
    #     easein 0.05 xpos 0.5405 alpha 0.0
    #     easein 0.2 xpos 0.5305 alpha 1.0
    # transform an_slmenu411:
    #     xpos 0.6 alpha 0.0
    #     easein 0.05 xpos 0.6 alpha 0.0
    #     easein 0.2 xpos 0.59 alpha 1.0
    # transform an_slmenu_text4:
    #     xpos 0.62 ypos 0.105 alpha 0.0 rotate 12
    #     easein 0.2 pass
    #     easein 0.3 xpos 0.50 alpha 1.0
    #     easein 0.2 xpos 0.52 alpha 1.0
    #
    # transform an_slmenu3:
    #     xpos 0.36 alpha 0.0
    #     easein 0.2 xpos 0.36 alpha 0.0
    #     easein 0.2 xpos 0.35 alpha 1.0
    #     block:
    #         on hover:
    #             easein 0.2 alpha 0.8
    #         on idle:
    #             easein 0.2 alpha 1.0
    # transform an_slmenu31:
    #     xpos 0.3705 alpha 0.0
    #     easein 0.15 xpos 0.3705 alpha 0.0
    #     easein 0.2 xpos 0.3605 alpha 1.0
    # transform an_slmenu311:
    #     xpos 0.425 alpha 0.0
    #     easein 0.15 xpos 0.425 alpha 0.0
    #     easein 0.2 xpos 0.415 alpha 1.0
    # transform an_slmenu_text3:
    #     xpos 0.745 ypos 0.48 alpha 0.0 rotate 12
    #     easein 0.2 pass
    #     easein 0.3 xpos 0.53 alpha 1.0
    #     easein 0.2 xpos 0.55
    # transform an_slmenu2:
    #     ypos 0.0 alpha 0
    #     easein 0.2 xpos 0.18 alpha 1.0
    #     block:
    #         on hover:
    #             easein 0.2 alpha 0.8
    #         on idle:
    #             easein 0.2 alpha 1.0
    #
    # transform an_slmenu21:
    #     xpos 0.2005 alpha 0.0
    #     easein 0.25 xpos 0.2005 alpha 0.0
    #     easein 0.2 xpos 0.1905 alpha 1.0
    # transform an_slmenu211:
    #     xpos 0.262 alpha 0.0
    #     easein 0.25 xpos 0.262 alpha 0.0
    #     easein 0.2 xpos 0.252 alpha 1.0
    # transform an_slmenu_text2:
    #     xpos 0.85 ypos 0.11 alpha 0.0 rotate 12
    #     easein 0.3 xpos 0.77 alpha 1.0
    #     easein 0.2 xpos 0.8

    transform an_slmenu1:
        ypos -0.1 alpha 0
        ease 0.3 ypos 0.15 alpha 1.0
        ease 0.2 ypos 0.13
        block:
            on hover:
                easein 0.2 alpha 0.8
            on idle:
                easein 0.2 alpha 1.0
    transform an_slmenu11:
        ypos -0.1 alpha 0
        ease 0.3 ypos 0.155 alpha 1.0
        ease 0.2 ypos 0.135
    transform an_slmenu111:
        ypos 0.72 alpha 0
        ease 0.3 ypos 0.865 alpha 1.0
        ease 0.2 ypos 0.84
    transform an_slmenu_text1:
        ypos 0.67 alpha 0.0
        ease 0.3 ypos 0.815 alpha 1.0
        ease 0.2 ypos 0.795





    transform an_loadsave:
        ypos 0.17 alpha 0
        ypos 0.2 alpha 1
        block:
            on hover:
                easein 0.1 ypos 0.15
            on idle:
                easein 0.1 ypos 0.2
    transform zmenu:
        alpha 0 xpos 0.28 ypos 0.4##a##
        ease 0.5 alpha 1 xpos 0.24
        block:
            zoom 1.0
            on hover:
                ease 0.1 zoom 0.95
            on idle:
                ease 0.1 zoom 1.0
    transform zmenu1:
        xpos 0.4 alpha 0 ypos 0.4##a##
        easein 0.1 alpha 0
        easein 0.5 alpha 1 xpos 0.46
        block:
            zoom 1.0
            on hover:
                ease 0.1 zoom 0.95
            on idle:
                ease 0.1 zoom 1.0
    transform zmenu2:
        xpos 0.6 alpha 0 ypos 0.4##a##
        easein 0.3 alpha 0
        easein 0.5 alpha 1 xpos 0.66
        block:
            zoom 1.0
            on hover:
                ease 0.1 zoom 0.95
            on idle:
                ease 0.1 zoom 1.0

    transform zmenu3:
        xpos 0.75 alpha 0 ypos 0.6##b##
        easein 0.5 alpha 1 xpos 0.66
        block:
            zoom 1.0
            on hover:
                ease 0.1 zoom 0.95
            on idle:
                ease 0.1 zoom 1.0
    transform zmenu4:
        xpos 0.6 alpha 0 ypos 0.6##b##
        ease 0.1 alpha 0
        easein 0.5 alpha 1 xpos 0.46
        block:
            zoom 1.0
            on hover:
                ease 0.1 zoom 0.95
            on idle:
                ease 0.1 zoom 1.0
    transform zmenu5:
        xpos 0.4 alpha 0 ypos 0.6##b##
        easein 0.3 alpha 0
        easein 0.5 alpha 1 xpos 0.24
        block:
            zoom 1.0
            on hover:
                ease 0.1 zoom 0.95
            on idle:
                ease 0.1 zoom 1.0
    transform zmenu6b:
        xpos 0.46 alpha 0 ypos 0.8##b##
        easein 0.3 alpha 0
        easein 0.5 alpha 1 ypos 0.83
        block:
            zoom 1.0
            on hover:
                ease 0.1 zoom 0.95 xpos 0.461
            on idle:
                ease 0.1 zoom 1.0 xpos 0.46

    transform anlo1:
        xalign 0.9 yalign 0.5 alpha 0.0##b##
        easein 0.4 alpha 0
        easein 0.5 alpha 1 xalign 0.86
        block:
            zoom 1.0
            on hover:
                ease 0.2 zoom 0.95
            on idle:
                ease 0.2 zoom 1.0
    transform anlo2:
        xalign 0.82 yalign 0.22 alpha 0.0##b## Save
        easein 0.2 alpha 0
        easein 0.5 alpha 1 xalign 0.8
        block:
            zoom 1.0
            on hover:
                ease 0.2 zoom 0.95
            on idle:
                ease 0.2 zoom 1.0
    transform anlo3:
        xalign 0.94 yalign 0.3 alpha 0.0##b## Load
        easein 0.3 alpha 0
        easein 0.5 alpha 1 xalign 0.92
        block:
            zoom 1.0
            on hover:
                ease 0.2 zoom 0.95
            on idle:
                ease 0.2 zoom 1.0
    transform anlo4:
        xalign 0.9 yalign 0.66 alpha 0.0##b##
        easein 0.5 alpha 0
        easein 0.5 alpha 1 xalign 0.86
        block:
            zoom 1.0
            on hover:
                ease 0.2 zoom 0.95
            on idle:
                ease 0.2 zoom 1.0
    transform anlo5:
        xalign 0.9 yalign 0.86 alpha 0.0##b##
        easein 0.6 alpha 0
        easein 0.5 alpha 1 xalign 0.86
        block:
            zoom 1.0
            on hover:
                ease 0.2 zoom 0.95
            on idle:
                ease 0.2 zoom 1.0

    transform exitm1:
        xpos 0.4 ypos .5 alpha 0.0 rotate 10##b##
        easein 0.3 alpha 0
        easein 0.5 alpha 1 xalign 0.35 rotate 0
        block:
            zoom 1.0
            on hover:
                ease 0.1 zoom 0.95
            on idle:
                ease 0.1 zoom 1.0
    transform exitm2:
        xpos 0.5 ypos .5 alpha 0.0 rotate 10##b##
        easein 0.3 alpha 0
        easein 0.5 alpha 1 xalign 0.63 rotate 0
        block:
            zoom 1.0
            on hover:
                ease 0.1 zoom 0.95
            on idle:
                ease 0.1 zoom 1.0

    transform time_day_anim_0:
        xpos 0.014 ypos 0.67 rotate -50
    transform time_day_anim_1:
        xpos 0.014 ypos 0.67 rotate -50
        ease 0.2 xpos 0.013 ypos 0.67 rotate 0
    transform time_day_anim_2:
        xpos 0.013 ypos 0.67 rotate 0
        ease 0.2 xpos 0.013 ypos 0.67 rotate 50
    transform time_day_anim_3:
        xpos 0.013 ypos 0.67 rotate 50
        ease 0.2 xpos 0.013 ypos 0.67 rotate 90
    transform time_day_anim_4:
        xpos 0.013 ypos 0.67 rotate 90
        ease 0.2 xpos 0.013 ypos 0.67 rotate 120
    transform time_day_anim_5:
        xpos 0.013 ypos 0.67 rotate 120
        ease 0.2 xpos 0.013 ypos 0.67 rotate 180
    transform time_day_anim_6:
        xpos 0.013 ypos 0.67 rotate 180
        ease 0.2 xpos 0.013 ypos 0.67 rotate 230
    transform time_day_anim_7:
        xpos 0.013 ypos 0.67 rotate 230
        ease 0.2 xpos 0.013 ypos 0.67 rotate 275


    transform suttm1:
        alpha 0 xpos -0.1
        ease 0.3 alpha 1 xpos 0.0
        block:
            zoom 1.0
            on hover:
                ease 0.1 zoom 0.95
            on idle:
                ease 0.1 zoom 1.0
    transform suttm2:
        alpha 0 xpos -0.1
        ease 0.1 alpha 0
        ease 0.3 alpha 1 xpos 0.0
        block:
            zoom 1.0
            on hover:
                ease 0.1 zoom 0.95
            on idle:
                ease 0.1 zoom 1.0
    transform suttm3:
        alpha 0 xpos -0.1
        ease 0.2 alpha 0
        ease 0.3 alpha 1 xpos 0.0
        block:
            zoom 1.0
            on hover:
                ease 0.1 zoom 0.95
            on idle:
                ease 0.1 zoom 1.0

    transform dissmenu:
        alpha 0
        ease 0.1 alpha 1
    transform dissmenu1:
        alpha 0
        ease 0.1 alpha 1
    transform dissmenu2:
        alpha 0 xpos 0.02 ypos 0.02
        ease 0.3 alpha 1 xalign 0.0 yalign 0.0
    transform dissmenu25:
        alpha 0
        ease 0.2 alpha 0
        ease 0.4 alpha 1
    transform dissmenu3:
        alpha 0 zoom 0.95 xalign 0.99 ypos 0.02
        ease 0.3 alpha 1 zoom 1.05 xalign 0.97 ypos -0.04

    transform alphabatt:
        alpha 0
        ease 0.3 alpha 1
        block:
            ease 1 alpha 1
            ease 1 alpha 0.9
            ease 1 alpha 1
            ease 1 alpha 0.8
            repeat

    transform batton_p:
        zoom 1.3 alpha 0.8 xpos 0.35
        on hover:
            ease 0.1 zoom 1.2 alpha 1.0 xpos 0.4
        on idle:
            ease 0.1 zoom 1.3 alpha 0.8 xpos 0.35

    transform batton1:
        zoom 1.0 alpha 0.9 rotate 0
        on hover:
            ease 0.1 zoom 1.1 alpha 1.0
            ease 0.4 zoom 1.08 alpha 0.8
            ease 0.4 zoom 1.1 alpha 1.0
            repeat
        on idle:
            ease 0.1 zoom 1.0 alpha 0.9 rotate 0

    transform alb_menu_butt_anim_1:
        zoom 1.0 xalign 0.1 alpha 0.6
        on hover:
            ease 0.2 zoom 1.05 xalign 0.07 alpha 1.0
        on idle:
            ease 0.2 zoom 1.0 xalign 0.1 alpha 0.6
    transform alb_menu_butt_anim_2:
        zoom 1.0 xalign 0.36 alpha 0.6
        on hover:
            ease 0.2 zoom 1.05 xalign 0.38 alpha 1.0
        on idle:
            ease 0.2 zoom 1.0 xalign 0.36 alpha 0.6
    transform alb_menu_butt_anim_3:
        zoom 1.0 yalign 0.785 alpha 0.6
        on hover:
            ease 0.2 zoom 1.05 yalign 0.83 alpha 1.0
        on idle:
            ease 0.2 zoom 1.0 yalign 0.785 alpha 0.6
    transform alb_menu_butt_anim_4:
        zoom 1.0 yalign 0.22 alpha 0.6
        on hover:
            ease 0.2 zoom 1.05 yalign 0.17 alpha 1.0
        on idle:
            ease 0.2 zoom 1.0 yalign 0.22 alpha 0.6



    transform bird1:
        alpha 0
        choice:
            linear 35 alpha 0
        choice:
            linear 10 alpha 0
        choice:
            linear 25 alpha 0

        choice:
            linear 8 alpha 0
            xpos 0.1 ypos 0.6 alpha 0
            linear 4 xpos 0.3 ypos 0.4 alpha 1
            linear 2 xpos 0.4 ypos 0.3 alpha 0
        choice:
            linear 3 alpha 0
            xpos 0.2 ypos 0.5 alpha 0
            linear 4 xpos 0.4 ypos 0.3 alpha 1
            linear 2 xpos 0.5 ypos 0.2 alpha 0
        choice:
            linear 7 alpha 0
            xpos 0.4 ypos 0.7 alpha 0
            linear 4 xpos 0.6 ypos 0.5 alpha 1
            linear 2 xpos 0.7 ypos 0.4 alpha 0
        choice:
            linear 35 alpha 0
        choice:
            linear 10 alpha 0
        choice:
            linear 25 alpha 0
        repeat

    transform bird2:
        alpha 0
        choice:
            linear 35 alpha 0
        choice:
            linear 10 alpha 0
        choice:
            linear 25 alpha 0
        choice:
            linear 16 alpha 0
            xpos 0.5 ypos 0.7 alpha 0
            linear 4 xpos 0.65 ypos 0.5 alpha 1
            linear 4 xpos 0.8 ypos 0.3 alpha 0
        choice:
            linear 13 alpha 0
            xpos 0.2 ypos 0.8 alpha 0
            linear 4 xpos 0.35 ypos 0.6 alpha 1
            linear 4 xpos 0.5 ypos 0.4 alpha 0
        repeat

    transform white1:
        alpha 0
        choice:
            linear 35 alpha 0
        choice:
            linear 10 alpha 0
        choice:
            linear 25 alpha 0
        choice:
            linear 3 alpha 0
            xpos 0.11 ypos 0.61 alpha 0
            linear 17 xpos 0.3 ypos 0.5 alpha 0.7
            linear 28 xpos 0.8 ypos 0.2 alpha 0
        choice:
            linear 2 alpha 0
            xpos 0.51 ypos 0.71 alpha 0
            linear 17 xpos 0.66 ypos 0.5 alpha 0.7
            linear 24 xpos 0.8 ypos 0.4 alpha 0
        repeat
    transform white2:
        alpha 0
        choice:
            linear 7 alpha 0
        choice:
            linear 10 alpha 0
        choice:
            linear 15 alpha 0

        choice:
            linear 4 alpha 0
            alpha 0
            xpos 0.31 ypos 0.61 alpha 0
            linear 17 xpos 0.45 ypos 0.3 alpha 0.7
            linear 20 xpos 0.6 ypos 0.2 alpha 0
        choice:
            linear 6 alpha 0
            xpos 0.11 ypos 0.61 alpha 0
            linear 17 xpos 0.3 ypos 0.3 alpha 0.7
            linear 20 xpos 0.5 ypos 0.2 alpha 0
        choice:
            linear 2 alpha 0
            xpos 0.51 ypos 0.81 alpha 0
            linear 17 xpos 0.7 ypos 0.6 alpha 0.7
            linear 20 xpos 0.9 ypos 0.4 alpha 0
        repeat

    transform ing_butt:
        zoom 1.0 alpha 0.6
        on hover:
            ease 0.2 zoom 1.05 alpha 1.0
        on idle:
            ease 0.2 zoom 1.0 alpha 0.6

    transform d_eff1:
        alpha .0 zoom 1.0 xpos -0.24 ypos -0.8 rotate 0 zoom 1.0
        block:
            ease 2.2 alpha .2 rotate 5 zoom 1.1
            ease 4.2 alpha .1 rotate -5 zoom 1.0
            repeat
        # block:
        #     ease 0.2 alpha .6 blur 1
        #     ease 2 alpha 0.4 blur 5 xalign 1.0
        #     ease 3 alpha .6 blur 1 xalign 1.1
    transform d_eff2:
        zoom 1.1 alpha 0.0 ypos -0.1
        block:
            ease 0.2 alpha 0.5 blur 5 xpos 0.0
            ease 8 alpha 0.3 blur 1 xpos -0.05
            ease 4 alpha .5 blur 5 xpos 0.0
            repeat

    transform ing_butt_text:
        zoom 1.0 alpha 0.0
        ease 0.2 alpha 1

    transform ing_butt_1:
        zoom 1.0 alpha 0.0 zoom 0.98
        ease 0.2 alpha 1 zoom 1
        on hover:
            ease 0.2 zoom 1.03
        on idle:
            ease 0.2 zoom 1.0

    transform inv_menu_ef:
        alpha 0 zoom 0.99
        ease 0.2 alpha 1 zoom 1
    transform inv_menu_ef1:
        alpha 0
        ease 0.2 alpha 1

    transform map_clock:
        alpha 0 xpos -0.01 zoom 0.98
        ease 0.2 alpha 1 zoom 1 xpos 0.0

    transform r_home_ef1:
        ypos 0.01 xpos -0.01 alpha 0 zoom 1.01
        ease 0.2 xpos 0.0 alpha 1 zoom 1.0 ypos 0.0

    transform r_home_ef2:
        xpos -0.01 alpha 0 zoom 1.01
        ease 0.2 xpos 0.0 alpha 1 zoom 1.0 ypos 0.0

    transform r_home_ef3:
        xpos -0.01 alpha 0 zoom 1.01
        ease 0.2 xpos 0.0 alpha 1 zoom 1.0 ypos 0.0

    image qtyo1:
        "images/effect/qtyo.png"
        ypos .4 xpos .0 alpha 0
        linear 1 ypos .4 xpos .0 alpha 1
        linear 3 ypos .4 xpos 0.8 alpha 1
        linear 1 ypos .4 xpos 1.0 alpha 0
        repeat
        #zoom 0.5 anchor(.5, .5)
    transform qtyz_button:
        pos(0.0, 0.4)
        #repeat
    transform qtypi_ef:
        ypos 1.0 xpos -0.2 alpha 0
        linear 0.5 alpha 1
        linear 0.5 alpha 0
        repeat
    transform moving_button:
        pos(0.5, 0.4) alpha 0
        linear 1.0 pos(0.0, 0.4) alpha 1.0
        linear 2.0 pos(-0.2, 0.4) alpha 1.0
        linear 1.0 pos(-0.5, 0.4) alpha 0.0
        repeat

    screen qte_imagemaps:
        #modal True
        #default timeout = 3
        #timer timeout action Hide("qte_imagemaps")
        add "qtyz" at qtyz_button
        imagebutton:
            #xalign .5 yalign .5
            auto "images/effect/qtyo_%s.png"
            at moving_button
            action Jump("glava3_day3_night_1")

    transform lite_batt:
        alpha 0.2 xalign 0.819 yalign 0.3
        block:
            ease 2 alpha 1
            ease 0.7 alpha 0.3
            ease 3 alpha 1
            ease 2 alpha 1
            repeat
    transform alpha1:
        alpha 0.2
        block:
            ease 5 alpha 0.8
            ease 2 alpha 0.2
            ease 4 alpha 0.8
            ease 2 alpha 0.4
            repeat
    transform alpha2:
        alpha 1
        block:
            ease 2 alpha 0.8
            ease 5 alpha 1
            ease 2 alpha 0.7
            ease 6 alpha 1
            repeat
    transform blurmenu:
        blur 0.2 zoom 1.1 xpos 0.0
        block:
            ease 2 blur 5 zoom 1.1 xpos 0.0
            ease 8 blur 5 zoom 1.1 xpos 0.0
            ease 3 blur 1 xpos -0.05
            ease 5 blur 3 zoom 1.2 xpos 0.0
            ease 2 blur 0.1 xpos -0.05
            ease 5 blur 5 zoom 1.1 xpos 0.0
            ease 8 blur 5 zoom 1.1 xpos 0.0
            ease 3 blur 1 xpos 0.0
            ease 5 blur 3 zoom 1.2 xpos -0.05
            ease 2 blur 0.1 xpos -0.05
            repeat
    transform bzan:
        yalign 0.5 alpha 0.3 alpha .5
        linear 0.2 yalign 0.6 alpha 0.3
        linear .01 alpha 0
        linear 5 alpha 0
        repeat

    transform lite:
        zoom 2 ypos -0.8 xpos -0.3
        block:
            easein 7.25 ypos -0.7 xpos -0.5
            easein 8.25 ypos -0.9 xpos -0.1
            easeout 10.25 ypos -0.8 xpos -0.3
            repeat

    transform my_tr:
        on show:
            alpha 0.0
            xoffset -20
            linear 0.5 alpha 1.0 xoffset 0
        on hide:
            linear 0.5 alpha 0.0 xoffset 20

    # отзеркаливание
    transform hflip():
        xzoom -1.0
    transform vflip():
        yzoom -1.0

    # подпрыгивание персонажа
    transform leap(dyz=0.01, dxz=0.005, dt=.4):
        yzoom 1.0
        easein dt*0.25 yzoom 1.0+dyz xzoom 1.0-dxz
        easeout dt*0.25 yzoom 1.0 xzoom 1.0
        easein dt*0.25 yzoom 1.0-dyz xzoom 1.0+dxz
        easeout dt*0.25 yzoom 1.0 xzoom 1.0
    # подпрыгивание персонажа
    transform leap00(dyz=0.01, dxz=0.005, dt=.4):
        xpos 0.4 ypos -0.07 zoom 3
        block:
            easein dt*6.25 xpos 0.4 ypos -0.07
            easein dt*6.25 xpos 0.42 ypos -0.07
            repeat

    transform leap0(dyz=0.01, dxz=0.005, dt=.4):
        easein dt*2.25 yzoom 1.0 xpos 0.6
        easeout dt*2.25 yzoom 1.0 xpos 0.595
        easein dt*2.25 yzoom 1.0 xpos 0.61
        easeout dt*2.25 yzoom 1.0 xpos 0.605
        easein dt*2.25 yzoom 1.0 xpos 0.6
        easeout dt*2.25 yzoom 1.0 xpos 0.595
        easein dt*2.25 yzoom 1.0 xpos 0.61
        easeout dt*2.25 yzoom 1.0 xpos 0.605
        easein dt*2.25 yzoom 1.0 xpos 0.6
        easeout dt*2.25 yzoom 1.0 xpos 0.595
        easein dt*2.25 yzoom 1.0 xpos 0.61
        easeout dt*2.25 yzoom 1.0 xpos 0.605
        yzoom 1.0
        easein dt*0.25 yzoom 1.0+dyz xzoom 1.0-dxz
        easeout dt*0.25 yzoom 1.0 xzoom 1.0
        easein dt*0.25 yzoom 1.0-dyz xzoom 1.0+dxz
        easeout dt*0.25 yzoom 1.0 xzoom 1.0
        repeat
    # подпрыгивание персонажа
    transform leap1(dyz=0.01, dxz=0.005, dt=.4):
        yzoom 1.0
        easein dt*0.25 yzoom 1.0+dyz xzoom 1.0-dxz
        easeout dt*0.25 yzoom 1.0 xzoom 1.0
        easein dt*0.25 yzoom 1.0-dyz xzoom 1.0+dxz
        easeout dt*0.25 yzoom 1.0 xzoom 1.0
        repeat

    # подпрыгивание персонажа
    transform leap2(dyz=0.01, dxz=0.005, dt=.4):
        yzoom 1.0
        easein dt*0.25 yzoom 1.0+dyz xzoom 1.0-dxz
        easeout dt*0.25 yzoom 1.0 xzoom 1.0
        easein dt*0.25 yzoom 1.0-dyz xzoom 1.0+dxz
        easeout dt*0.25 yzoom 1.0 xzoom 1.0
        yzoom 1.0
        easein dt*0.25 yzoom 1.0+dyz xzoom 1.0-dxz
        easeout dt*0.25 yzoom 1.0 xzoom 1.0
        easein dt*0.25 yzoom 1.0-dyz xzoom 1.0+dxz
        easeout dt*0.25 yzoom 1.0 xzoom 1.0
        yzoom 1.0
        easein dt*0.25 yzoom 1.0+dyz xzoom 1.0-dxz
        easeout dt*0.25 yzoom 1.0 xzoom 1.0
        easein dt*0.25 yzoom 1.0-dyz xzoom 1.0+dxz
        easeout dt*0.25 yzoom 1.0 xzoom 1.0
        yzoom 1.0
        easein dt*0.25 yzoom 1.0+dyz xzoom 1.0-dxz
        easeout dt*0.25 yzoom 1.0 xzoom 1.0
        easein dt*0.25 yzoom 1.0-dyz xzoom 1.0+dxz
        easeout dt*0.25 yzoom 1.0 xzoom 1.0


    # относительное положение на экране по х(/y)-координате
    transform at_axy(ax=.5, ay=1.0):
        align (ax, ay)

    # вращение вокруг указанной точки
    transform at_rot(x=0, y=0, delay=30, xa=.5, ya=.5):
        rotate 0.0
        anchor(xa, ya)
        pos(x, y)
        linear delay rotate 360
        repeat

    # слева, но не у самого края
    transform left2(xa=.35):
        xalign xa xanchor .5 ypos 1.0 yanchor 1.0

    # справа, но не у самого края
    transform right2(xa=.65):
        xalign xa xanchor .5 ypos 1.0 yanchor 1.0

    # слева, за краем
    transform left0():
        xpos .0 xanchor 1.0 ypos 1.0 yanchor 1.0

    # справа, за краем
    transform right0():
        xpos 1.0 xanchor .0 ypos 1.0 yanchor 1.0

    # однократное спрайтотрясение
    transform shake(dt=.05, dxy=10, dxy_from=5):
        xoffset rnd(dxy_from, dxy) - rnd(dxy_from, dxy) yoffset rnd(dxy_from, dxy)
        pause dt
        xoffset rnd(dxy_from, dxy) - rnd(dxy_from, dxy) yoffset rnd(dxy_from, dxy)
        pause dt
        xoffset rnd(dxy_from, dxy) - rnd(dxy_from, dxy) yoffset rnd(dxy_from, dxy)
        pause dt
        xoffset rnd(dxy_from, dxy) - rnd(dxy_from, dxy) yoffset rnd(dxy_from, dxy)
        pause dt
        xoffset rnd(dxy_from, dxy) - rnd(dxy_from, dxy) yoffset rnd(dxy_from, dxy)
        pause dt
        xoffset rnd(dxy_from, dxy) - rnd(dxy_from, dxy) yoffset rnd(dxy_from, dxy)
        pause dt
        xoffset rnd(dxy_from, dxy) - rnd(dxy_from, dxy) yoffset rnd(dxy_from, dxy)
        pause dt
        xoffset rnd(dxy_from, dxy) - rnd(dxy_from, dxy) yoffset rnd(dxy_from, dxy)
        pause dt
        xoffset rnd(dxy_from, dxy) - rnd(dxy_from, dxy) yoffset rnd(dxy_from, dxy)
        pause dt
        xoffset rnd(dxy_from, dxy) - rnd(dxy_from, dxy) yoffset rnd(dxy_from, dxy)
        pause dt
        xoffset 0 yoffset 0
        pause dt

    # увеличение/уменьшение в центре экрана
    transform wowrun(dt=.25, z=1.25):
        anchor(.5, .5) align(.5, .5) zoom 1
        ease dt*1 anchor(.5, .5) align(.5, .5) zoom 1.05 xpos .51 ypos .51
        ease dt*2 anchor(.5, .5) align(.5, .5) zoom 1.07 xpos .52 ypos .5
        ease dt*2 anchor(.5, .5) align(.5, .5) zoom 1.02 xpos .51 ypos .49
        ease dt*1 anchor(.5, .5) align(.5, .5) zoom 1.05 xpos .49 ypos .50
        ease dt*2 anchor(.5, .5) align(.5, .5) zoom 1
        repeat

    transform wow(dt=.25, z=1.25):
        anchor(.5, .5) align(.5, .5) zoom 1.0
        easeout dt*.5 anchor(.5, .5) align(.5, .5) zoom z
        easein dt*.5 anchor(.5, .5) align(.5, .5) zoom 1.0
        repeat

    transform wow1(dt=.25, z=1.25):
        anchor(.5, .5) align(.5, .5) zoom 1.0
        easeout dt*5.5 anchor(.5, .5) align(.5, .5) zoom 1.01 xpos .51
        easeout dt*5.5 anchor(.5, .5) align(.5, .5) zoom 1.015 xpos .52
        easeout dt*5.5 anchor(.5, .5) align(.5, .5) zoom 1.01 xpos .51
        easeout dt*5.5 anchor(.5, .5) align(.5, .5) zoom 1.015 xpos .48
        easeout dt*5.5 anchor(.5, .5) align(.5, .5) zoom 1.0
        repeat
    transform wow2(dt=.25, z=1.25):
        anchor(.5, .5) align(.5, .5) zoom 1.1
        easeout dt*5 anchor(.5, .5) align(.5, .5) zoom 1.1 xpos .51 ypos .51
        easeout dt*5 anchor(.5, .5) align(.5, .5) zoom 1.115 xpos .52 ypos .5
        easeout dt*5 anchor(.5, .5) align(.5, .5) zoom 1.11 xpos .51 ypos .49
        easeout dt*5 anchor(.5, .5) align(.5, .5) zoom 1.115 xpos .48 ypos .51
        easeout dt*5 anchor(.5, .5) align(.5, .5) zoom 1.1
        repeat

    transform wow3(dt=.25, z=1.25):
        ease dt*15 anchor(.5, .5) align(.5, .5) zoom 1.1
        ease dt*15 anchor(.5, .5) align(.5, .5) zoom 1.3 xpos .5 ypos .6
        ease dt*15 anchor(.5, .5) align(.5, .5) zoom 1.3 xpos .5 ypos .58
        ease dt*15 anchor(.5, .5) align(.5, .5) zoom 1.3 xpos .5 ypos .6
        ease dt*15 anchor(.5, .5) align(.5, .5) zoom 1.3 xpos .5 ypos .58
        ease dt*15 anchor(.5, .5) align(.5, .5) zoom 1.3 xpos .5 ypos .6
        ease dt*15 anchor(.5, .5) align(.5, .5) zoom 1.3 xpos .5 ypos .58

    transform wow4(dt=.25, z=1.25):
        anchor(.5, .5) align(.5, .5) zoom 1.3 xpos .5 ypos .58
        ease dt*70 anchor(.5, .5) align(.5, .5) zoom 1.5 xpos .5 ypos .3

    # выстрел по дуге
    transform bow(x1, y1, x2, y2, dy=300, dt=1.0, rot=0):
        pos(x1, y1) anchor(.5, .5) alpha 1.0 rotate 0
        parallel:
            alpha .0
            easein dt*.15 alpha 1.0
            pause dt*.7
            easein dt*.15 alpha .0
        parallel:
            linear dt xpos x2 rotate rot
        parallel:
            easein dt*.5 ypos(-dy+(y1+y2)/2)
            easeout dt*.5 ypos(y2)

init -999 python:
    # сканируем папку музыки, на выходе - список мелодий без указанного расширения и папки
    def nvl_cls(effect=dissolve):
        global nvl
        nvl = []


    def get_music_list(folder="music", ext="ogg"):
        res = []
        list = renpy.list_files()
        for i in list:
            if i.startswith(folder):
                s = i[(len(folder) + 1):]
                if s.endswith("." + ext):
                    res.append(s[:(-len(ext) - 1)])
        return res

    # сканируем папку, на выходе - список файлов нужного расширения
    # по умолчанию расширения убираются
    def get_file_list(folder="", ext="", hideext=True):
        res = []
        list = renpy.list_files()
        for i in list:
            if i.startswith(folder) or (not folder):
                if folder:
                    s = i[(len(folder) + 1):]
                else:
                    s = i
                if ext:
                    if s.endswith("." + ext):
                        if hideext:
                            s = s[:(-len(ext) - 1)]
                        res.append(s)
                else:
                    res.append(s)
        if len(res) > 1:
            # сортировка без учета регистра
            res = sorted(res, key=lambda s: s.lower())
        return res

    # получить цвета для матрицы
    def get_rgba(color):
        col = Color(color)
        rgb = col.rgb
        return rgb[0], rgb[1], rgb[2], col.alpha

    # получить спрайт с искажением цветов
    def LiveMatrix(img, matrix):
        return im.MatrixColor(img, matrix)

    # получить спрайт с искажением цветов
    def LiveTint(img, r=1.0, g=1.0, b=1.0):
        return LiveMatrix(img, im.matrix.tint(r, g, b))

    # изменить насыщенность
    def LiveSaturation(img, saturation=.01):
        return LiveMatrix(img, im.matrix.saturation(saturation))

    def LiveSaturation1(img, saturation=.4, bright=.3):
        return LiveMatrix(img, im.matrix.saturation(saturation))
    def LiveSaturation2(img, saturation=.5, bright=.3):
        return LiveMatrix(img, im.matrix.saturation(saturation))


    # изменить контрастность
    def LiveContrast(img, contrast=1.1):
        return LiveMatrix(img, im.matrix.contrast(contrast))

    # изменить яркость
    def LiveBright(img, bright=.1):
        return LiveMatrix(img, im.matrix.brightness(bright))

    # силуэт спрайта
    # использовать в init 1901 и выше (после автообъявления изображений)
    def LiveShadow(img, color="#000"):
        r, g, b, a = get_rgba(color)
        return LiveMatrix(img, im.matrix((0, 0, 0, 0, r, 0, 0, 0, 0, g, 0, 0, 0, 0, b, 0, 0, 0, a, 0,)))

    # выстрел снарядом shell от перса spr_from к персу spr_to
    # по дуге высотой -dy
    def shoot(shell, spr_from, spr_to, dy=300, dt=1.0, rot=0, shell_as=None):
        if shell_as is None:
            shell_as = shell
        if spr_from == "left":
            x1, y1 = 0, config.screen_height / 2
        elif spr_from == "right":
            x1, y1 = config.screen_width / 2, config.screen_height / 2
        else:
            x, y, w, h = renpy.get_image_bounds(spr_from)
            x1, y1 = int(x + w/2), int(y + h/2)
        if spr_to == "left":
            x2, y2 = 0, config.screen_height / 2
        elif spr_to == "right":
            x2, y2 = config.screen_width / 2, config.screen_height / 2
        else:
            x, y, w, h = renpy.get_image_bounds(spr_to)
            x2, y2 = int(x + w/2), int(y + h/2)
        renpy.show(shell_as, what=shell, at_list=[bow(x1, y1, x2, y2, dy, dt, rot)])
        renpy.pause(dt)

    # сменить размер шрифта в игре
    # вызывать из init -1 python, не раньше
    def font_size(say=26, who=None, prf=None, mm=None):
        style.say_dialogue.size = say # текст в текстбоксе
        style.say_thought.size = say # текст в текстбоксе
        if not who is None:
            style.say_label.size = who # имя персонажа
        if not prf is None:
            # интерфейс (настройки и сохранения)
            style.pref_label_text.size = prf
            style.pref_button_text.size = prf
            style.small_button_text.size = prf
            style.large_button_text.size = prf
            style.file_picker_text.size = prf
            style.file_picker_button_text.size = prf
            style.file_picker_nav_button_text.size = prf
            style.button_text.size = prf # текст на кнопках
            style.label_text.size = prf # надписи
        if not mm is None:
            style.mm_button_text.size = mm # кнопки главного меню
        # применяем изменения
        style.rebuild()

    # окно игры в центре экрана (вызывается из init)
    def window_center():
        import os
        os.environ['SDL_VIDEO_CENTERED'] = '1'

    # автоматическое объявление изображений (вызывается из init)
    def images_auto(folders=["images", "gui"]):
        config.automatic_images_minimum_components = 1
        config.automatic_images = [' ', '_', '/']
        config.automatic_images_strip = folders

    # остановить перемотку
    def stop_skip():
        renpy.config.skipping = None

    # строку в displayable
    def img2disp(image):
        return renpy.easy.displayable(image)

    # узнать текущие размеры изображения типа displayable
    # например, после масштабирования и других операций
    # не работает в разделе init
    def get_size(displayable):
        return renpy.render(img2disp(displayable), 0, 0, 0, 0).get_size()
    def get_width(displayable):
        return get_size(displayable)[0]
    def get_height(displayable):
        return get_size(displayable)[1]

    # если это не список, то сделать единственным элементом списка
    def make_list(param):
        if param is None:
            return None
        if not isinstance(param, list):
            param = [param]
        return param

    # эффект dissolve, но с учетом прозрачности спрайта. пример:
    # with diss
    diss = Dissolve(.1, alpha=True)
    diss25 = Dissolve(.25, alpha=True)

    # эффект вспышки нужного цвета для смены фонов. пример:
    # with flash("#822")
    def flash(color="#fff", t=1.0, w=0):
        return Fade(t*.25, w, t*.75, color=color)

# автоматическое объявление анимации
    # описание функции Ani:
    # автоматическое объявление картинки с анимацией,
    # например есть кадры "images/neko%s.png",
    # где %s - числа от 1 до 5, тогда объявляем анимацию так:
    # image neko = Ani("neko", 5, 0.5, reverse = False)
    # где:
    # img_name - имя файла без номера (например, "neko")
    # frames - количество кадров
    # delay - пауза между кадрами в секундах
    # если delay это кортеж, например (1, 2), то скорость будет меняться от 1 до 2 секунд
    # loop - зациклить анимацию (по умолчанию включено)
    # reverse - нужно ли проигрывание анимации в обратную сторону
    # effect - эффект для смены кадров
    # start - с какой цифры начинать отсчет кадров
    # ext - расширение, если оно отлично от Null, то работаем с файлами,
    # при ext=Null - с displayable (уже объявленными или даже измененными изображениями)
    # так же можно добавлять любые стандартные для изображений параметры, типа масштабирования или прозрачности:
    # image neko = Ani("neko", 5, 0.5, zoom=2.0, alpha=0.75)
    def Ani(img_name, frames, delay=.1, loop=True, reverse=False, effect=diss, start=1, ext=None, **properties):
        args = []
        # если пауза переменная, то вычисляем ее шаг
        if isinstance(delay, tuple):
            d0 = delay[0]
            d1 = delay[1]
            f = (frames - 1)
            if f <= 0:
                dp = 0
            else:
                dp = (d1 - d0) * 1.0 / f
            delay = d0
        else:
            dp = 0
        # перебираем все кадры анимации
        for i in range(start, start + frames):
            if ext:
                img = renpy.display.im.image(img_name + str(i) + "." + ext)
            else:
                img = img2disp(img_name + str(i))
            img = Transform(img, **properties)
            args.append(img)
            if reverse or loop or (i < start + frames - 1):
                args.append(delay)
                delay += dp
                # добавляем эффект для смены кадров
                args.append(effect)
        if reverse: # обратная анимация, если нужна
            dp = -dp
            delay += dp
            for i in range(start + frames - 2, start, -1):
                if ext:
                    img = renpy.display.im.image(img_name + str(i) + "." + ext)
                else:
                    img = img2disp(img_name + str(i))
                img = Transform(img, **properties)
                args.append(img)
                if loop or (i > start + 1):
                    args.append(delay)
                    delay += dp
                    args.append(effect)
        return anim.TransitionAnimation(*args)

    # анимированная текстура с вырезанием по маске
    def AniMask(mask_name, img_name, frames, delay=.1, loop=True, reverse=False, effect=diss, start=1, ext=None, **properties):
        args = []
        # если пауза переменная, то вычисляем ее шаг
        if isinstance(delay, tuple):
            d0 = delay[0]
            d1 = delay[1]
            f = (frames - 1)
            if f <= 0:
                dp = 0
            else:
                dp = (d1 - d0) * 1.0 / f
            delay = d0
        else:
            dp = 0
        # перебираем все кадры анимации
        for i in range(start, start + frames):
            if ext:
                img = renpy.display.im.image(img_name + str(i) + "." + ext)
            else:
                img = img2disp(img_name + str(i))
            img = AlphaMask(img, img2disp(mask_name))
            img = Transform(img, **properties)
            args.append(img)
            if reverse or loop or (i < start + frames - 1):
                args.append(delay)
                delay += dp
                # добавляем эффект для смены кадров
                args.append(effect)
        if reverse: # обратная анимация, если нужна
            dp = -dp
            delay += dp
            for i in range(start + frames - 2, start, -1):
                if ext:
                    img = renpy.display.im.image(img_name + str(i) + "." + ext)
                else:
                    img = img2disp(img_name + str(i))
                img = AlphaMask(img, img2disp(mask_name))
                img = Transform(img, **properties)
                args.append(img)
                if loop or (i > start + 1):
                    args.append(delay)
                    delay += dp
                    args.append(effect)
        return anim.TransitionAnimation(*args)

    # показать фон с именем bg указанного цвета color
    def bg(color="#000", bg="bg"):
        renpy.scene()
        renpy.show(bg, what=img2disp(color))

    # меняем стандартное время всех или некоторых эффектов для появления/исчезновения спрайтов
    def move_time(delay=.5, effects=["move", "ease"]):
        effects = make_list(effects)
        for i in effects:
            define.move_transitions(i, delay)

    # для цифровых часиков (не менять, не вызывать)
    clock_properties = None
    def show_digital_clock(st, at):
        import datetime
        cur_time = datetime.datetime.now().strftime("%H:%M:%S")
        img = Text(cur_time, **clock_properties)
        return img, .25

    # создать цифровые часики с любым именем картинки (только в init!):
    # $ create_clock("digital_clock", size=48, color="#fff8", outlines=[(2, "#0008", 0, 0)], align=(.05, .05))
    # применение - на любом экране screen:
    # add "digital_clock"
    # или в виде спрайта:
    # show digital_clock
    def create_clock(name, **properties):
        global clock_properties
        clock_properties = properties
        renpy.image(name, DynamicDisplayable(show_digital_clock))

    # показать экран на слое "мастер",
    # чтобы он не исчезал, когда прячем интерфейс
    def show_s(screen, **kwarg):
        renpy.show_screen(screen, _layer="master", **kwarg)

    # убрать экран со слоя "мастер"
    def hide_s(screen, **kwarg):
        renpy.hide_screen(screen, layer="master", **kwarg)

    # показать рамку, неубирающуюся вместе с другими экранами
    # вызов: $ show_forever("имя_картинки_для_рамки")
    def show_forever(forever_frame):
        renpy.show_screen("forever_screen", forever_frame, _layer="foreverlayer")

    # спрятать рамку, неубирающуюся вместе с другими экранами
    def hide_forever():
        renpy.hide_screen("forever_screen", layer="foreverlayer")

    # получить английское название времени суток
    # если не указывать время в часах,
    # то будет взято системное время
    # можно задать начало утра, дня, вечера и ночи в часах от 0 до 23
    def time_of_day(hours=None, morning=7, day=11, evening=18, night=23):
        if hours is None:
            hours = int(datetime.datetime.now().strftime("%H"))
        res = "night" # по умолчанию ночь
        # границы любого времени суток можно поменять
        if (hours >= morning) and (hours <= day):
            res = "morning"
        if (hours > day) and (hours <= evening):
            res = "day"
        if (hours > evening) and (hours < night):
            res = "evening"
        return res

    # словарь цветов для времен суток
    color_filters = {"morning": "#8404", "day": "#0000", "evening": "#0484", "night": "#000b"}

    # получить цвет фильтра, соответствующий времени суток
    def color_of_day(hours=None):
        return color_filters[time_of_day(hours)]

    # действие - продолжить игру оттуда, где закончили
    # если загружать пока нечего, то кнопка неактивна
    # textbutton _("Продолжить игру") action Continue()
    class Continue(Action, DictEquality):
        def __call__(self):
            FileLoad(1, confirm=False, page="auto", newest=True)()
        # кликабельность кнопки
        def get_sensitive(self):
            return FileLoadable(1, page="auto")

    # объявлена ли картинка с именем name
    def has_image(name):
        for i in renpy.display.image.images:
            # такая конструкция позволяет исключить пустые теги
            if name == " ".join(" ".join(i).split()):
                return True
        return False

    # проверить существование нескольких изображений через запятую
    def has_images(*args):
        res = True
        for i in args:
            if isinstance(i, (list, dict)):
                res = res & has_images(i)
            else:
                res = res & has_image(i)
        return res

    # задан ли курсор с таким именем
    def has_mouse(mouse):
        if config.mouse:
            if mouse in config.mouse.keys():
                return True
        return False

    # рандомное целое число в заданных пределах
    # (i_to можно не указывать, тогда максимум берется из i_from)
    def rnd(i_from=0, i_to=None):
        if i_to is None:
            i_to = i_from
            i_from = 0
        return renpy.random.randint(int(i_from), int(i_to - 1))

    # рандомное дробное число в заданных пределах
    # (f_to можно не указывать, тогда максимум берется из f_from)
    def rndf(f_from=0, f_to=None):
        if f_to is None:
            f_to = f_from
            f_from = .0
        return f_from + renpy.random.random() * (f_to - f_from)

    # канал для эффекта
    renpy.music.register_channel("effect", "sfx", loop=True)

    # зацикленный звуковой эффект, не музыка
    def sfxplay(name, channel="effect", loop=True, fadein=0, fadeout=0, ext="ogg"):
        if name:
            renpy.music.play("sounds/" + name + "." + ext, channel=channel, loop=loop, fadein=fadein, fadeout=fadeout)

    # костыли для звуков и музыки - сокращают писанину
    # можно запускать музыку или звуки, не указывая папки и расширения
    # по умолчанию для музыки music/*.ogg
    # по умолчанию для звуков sounds/*.ogg

    # запустить музыку, если она еще не играет
    def mplay(mname, fadein=1.5, fadeout=1.5, loop=True, channel="music", ext="ogg"):
        old_fn = renpy.music.get_playing()
        new_fn = "music/"+ mname + "." + ext
        if mname:
            if old_fn != new_fn:
                renpy.music.play(new_fn, channel=channel, loop=loop, fadein=fadein, fadeout=fadeout)

    # перезапустить музыку, даже если уже играет она же
    def mreplay(mname, fadein=1.5, fadeout=1.5, loop=True, channel="music", ext="ogg"):
        new_fn = "music/"+ mname + "." + ext
        renpy.music.play(new_fn, channel=channel, loop=loop, fadein=fadein, fadeout=fadeout)

    # запустить музыку для имени файла и пути
    def fnplay(new_fn, fadein=1.5, fadeout=1.5, channel="music"):
        old_fn = renpy.music.get_playing()
        if old_fn != new_fn and new_fn:
            renpy.music.play(new_fn, channel=channel, loop=True, fadein=fadein, fadeout=fadeout)

    # последняя сохраненная мелодия
    last_music_fn = ""

    # сохранить в памяти играющую мелодию
    def msave():
        global last_music_fn
        last_music_fn = renpy.music.get_playing()

    # восстановить игравшую при сохранении мелодию
    def mrestore(fadein=1.5, fadeout=1.5, channel="music"):
        fnplay(last_music_fn, fadein=fadein, fadeout=fadeout, channel=channel)

    # воспроизвести звук для канала audio, который поддерживает многопоточность
    def splay(mname, fadein=0, fadeout=0, channel="audio", ext="ogg"):
        if mname:
            renpy.play("sounds/" + mname + "." + ext, channel=channel, fadein=fadein, fadeout=fadeout)

    # воспроизвести звук
    def sndplay(mname, fadein=0, fadeout=0, channel="sound", ext="ogg"):
        if mname:
            renpy.play("sounds/" + mname + "." + ext, channel=channel, fadein=fadein, fadeout=fadeout)

    # голос
    def vplay(mname, fadein=0, fadeout=0, channel="voice", ext="ogg"):
        if mname:
            renpy.play("voices/" + mname + "." + ext, channel=channel, fadein=fadein, fadeout=fadeout)

    # остановить звук
    def sstop(fadeout=None, channel='audio'):
        renpy.music.stop(channel=channel, fadeout=fadeout)

    # остановить звук
    def sndstop(fadeout=0, channel='sound'):
        renpy.music.stop(channel=channel, fadeout=fadeout)

    # остановить музыку
    def mstop(fadeout=1.5, channel='music'):
        renpy.music.stop(channel=channel, fadeout=fadeout)

    # остановить зацикленный эффект
    def sfxstop(fadeout=1.5, channel='effect'):
        renpy.music.stop(channel=channel, fadeout=fadeout)

    # превращаем функции в action для экранов screen
    SPlay = renpy.curry(splay)
    SFXPlay = renpy.curry(sfxplay)
    MPlay = renpy.curry(mplay)
    FNPlay = renpy.curry(fnplay)
    VPlay = renpy.curry(vplay)
    SStop = renpy.curry(sstop)
    MStop = renpy.curry(mstop)

    # установить громкость канала в коэффициенте от громкости звуков
    def sfxvolume(volume=1.0, channel='effect', delay=1.0):
        volume = _preferences.get_volume('sfx') * volume
        if volume < 0:
            volume = 0
        if volume > 1.0:
            volume = 1.0
        renpy.music.set_volume(volume, delay, channel=channel)

    import re

    # получить словарь с тегами и их значением
    def get_tags(text, prefix='#'):
        res = {}
        # выуживаем все теги ремарок
        tags = re.findall('{' + prefix + '([^}]+)}', text)
        # перебираем полученные теги
        for i in tags:
            parts = i.split('=')
            if len(parts) > 0:
                key = parts[0].strip()
                val = None
                if len(parts) > 1:
                    val = parts[1]
                # добавляем тэг и его значение в словарь
                res[key] = val
        # возвращаем значения тэгов в виде словаря
        return res

    # убрать все тэги из строки
    def del_tags(txt, prefix='#'):
        return re.sub(r'{' + prefix + '([^}]+)}', '', txt)

    # получить тэги и вернуть их в виде списка строк
    def get_tags_str(text, prefix='#'):
        # выуживаем все теги ремарок
        return re.findall('{' + prefix + '([^}]+)}', text)

    # разделить строку на две части - до и после знака равно
    # (или другого разделителя) и убрать пробелы вокруг этих частей
    def get_key_val(text, sep='='):
        txt = text.split(sep, 1)
        val, key = None, None
        if len(txt) > 0:
            key = txt[0].strip()
        if len(txt) > 1:
            val = txt[1].strip()
        return key, val

    # поиск в строке значения невидимого читателю тега
    # пример использования:
    # $ text = "Текст текст {#image=logo.png} текст."
    # $ img = get_tag(text, 'image')
    # на выходе в img будет logo.png
    def get_tag(text, tag, default=None, prefix='#'):
        tag = tag.strip()
        tags = get_tags(text, prefix)
        if tag in tags.keys():
            return tags[tag]
        return None

    # есть ли тэг в строке
    def have_tag(text, tag, prefix='#'):
        return tag in get_tags(text, prefix).keys()

    # получить цвета для матрицы
    def get_rgba(color):
        col = Color(color)
        rgb = col.rgb
        return rgb[0], rgb[1], rgb[2], col.alpha

    # показать спрайт с искажением цветов
    def LiveMatrix(img, matrix):
        return im.MatrixColor(img2disp(img), matrix)

    # изменить насыщенность
    def LiveBlind(img, blind=.01):
        return LiveMatrix(img, im.matrix.saturation(blind))

    # силуэт спрайта
    def LiveShadow(img, color="#000"):
        r, g, b, a = get_rgba(color)
        return LiveMatrix(img, im.matrix((0, 0, 0, 0, r, 0, 0, 0, 0, g, 0, 0, 0, 0, b, 0, 0, 0, a, 0,)))

    # скопировать текст в буфер
    import pygame.scrap
    def clip_copy(text):
        pygame.scrap.put(pygame.scrap.SCRAP_TEXT, text.encode("utf-8"))
        renpy.notify(pygame.scrap.get(pygame.scrap.SCRAP_TEXT))
    ClipCopy = renpy.curry(clip_copy)

    # получить текст из буфера
    def clip_past():
        return pygame.scrap.get(pygame.scrap.SCRAP_TEXT)

    # список слоев. наш экран не будет исчезать при нажатии 'h'
    config.layers.insert(config.layers.index("transient") + 1, "foreverlayer")

    # нужно включить автоматические сохранения, чтобы работала Continue (подставить = True)
    config.has_autosave = False

    # для input
    current_input_text = ""
    input_changes = False

    # функция вызова поля ввода с кнопками ок и отмена. пример:
    # $ s = input("Введите имя:", default="Аноним")
    def input(prompt=None, default=None, allow=None, caption_bg=None):
        global current_input_text, input_changes
        input_changes = False
        current_input_text = ""
        ShowMenu("my_input", prompt, default, allow, caption_bg)()
        if current_input_text is None:
            return None
        if not input_changes:
            current_input_text = default
        return current_input_text
    Input = renpy.curry(input)

    # функция вызова сообщения с кнопкой ок. пример:
    # $ message("Всё в норме.", size=26, color="#8a8")
    def message(message_text=" ", **args):
        ShowMenu("my_message", message_text, **args)()
    Message = renpy.curry(message)

    # узнать, что за символ введён или стёрт
    def input_changed(input_str):
        global current_input_text, input_changes
        current_input_text = input_str
        input_changes = True

init 1 python:
    # параметры текста для ввода
    style.input_text.xalign = .5
    style.input_text.font = style.say_dialogue.font
    style.input_text.size = style.say_dialogue.size

# экран ввода с кнопками ок и отмена
screen my_input(prompt=None, default=None, allow=None, caption_bg=None):
    modal True
    tag menu
    window style "gm_root":
        background "#0008" # необязательное затемнение экрана
        key "dismiss" action []
        key "input_enter" action Return()
        key "K_ESCAPE" action [SetVariable("current_input_text", None), Return()]
        frame:
            style_group "yesno"
            align (.5, .5)
            vbox align (.5, .5):
                spacing config.screen_width / 60
                if prompt:
                    frame:
                        if caption_bg:
                            background caption_bg
                        align (.5, .0) xminimum config.screen_width / 4
                        label prompt style "pref_label" xalign .5
                input id "input" style "input_text" changed input_changed default default allow allow
                hbox xalign .5:
                    textbutton _("OK") xalign .5 action Return()
                    textbutton _("Отмена") xalign .5 action [SetVariable("current_input_text", None), Return()]

# экран сообщения с кнопкой ок
screen my_message(message_text=" ", **args):
    modal True
    tag menu
    window style "gm_root":
        key "dismiss" action []
        key "input_enter" action Return()
        key "K_ESCAPE" action Return()
        frame:
            style_group "yesno"
            align (.5, .5)
            vbox align (.5, .5):
                spacing config.screen_width / 60
                xminimum config.screen_width / 4
                text " "
                label message_text style "pref_label" xalign .5
                textbutton _("OK") xalign .5 action Return()
                text " "

# экран для неубирающейся рамки
screen forever_screen (forever_frame, _layer="foreverlayer"):
    # выводится, если это игра, но не экран настроек
    if not ("preferences" in renpy.current_screen().screen_name):
        add forever_frame

# стандартное автообъявление картинок, но с webp
# выполняется после всего остального
init 1900 python hide:
    def create_automatic_images():
        seps = config.automatic_images
        if seps is True:
            seps = [ ' ', '/', '_' ]
        for dir, fn in renpy.loader.listdirfiles():
            if fn.startswith("_"):
                continue
            # Only .png and .jpg and .webp
            if not fn.lower().endswith(".png") and not fn.lower().endswith(".jpg") and not fn.lower().endswith(".webp"):
                continue
            # Strip the extension, replace slashes.
            shortfn = fn[:-4]
            if fn.lower().endswith(".webp"):
                shortfn = fn[:-5]
            shortfn = shortfn.replace("\\", "/")
            # Determine the name.
            name = ( shortfn, )
            for sep in seps:
                name = tuple(j for i in name for j in i.split(sep))
            # Strip name components.
            while name:
                for i in config.automatic_images_strip:
                    if name[0] == i:
                        name = name[1:]
                        break
                else:
                    break
            # Only names of 2 components or more by default.
            if len(name) < config.automatic_images_minimum_components:
                continue
            # Reject if it already exists.
            if name in renpy.display.image.images:
                continue
            renpy.image(name, fn)
    if config.automatic_images:
        create_automatic_images()

###############################################################################
# Pressable imagebuttons                                                      #
###############################################################################

#a string containing a button name ("button0" is NOT used for any buttons)
default button_number = "button0"

#define a name for the "_pressed" version of each button, for simplicity they
#should match the button names used by the imagebutton "auto"
image button1_pressed = Image("images/button1_pressed.png")
image button2_pressed = Image("images/button2_pressed.png")

#define a position for each button that will be on the screen
transform button1_pos:
    xalign 0.3
    ypos 550

transform button2_pos:
    xalign 0.7
    ypos 550

# This checks whether the left mouse button has been pressed, then displays
# the "_pressed" version of the button over it at the same position.
# It's based on the Konami Code cookbook entry.
init python hide:

    class ButtonListener(renpy.Displayable):

        def __init__(self):

            renpy.Displayable.__init__(self)

            import pygame

        # This function listens for events.
        def event(self, ev, x, y, st):
            import pygame
            LEFT = 1
            RIGHT = 3

            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == LEFT:
                #if the left mouse button is down, and we're on a non-zero button:
                if button_number != "button0":
                    renpy.notify("You're holding the button.")
                    renpy.show(store.button_number + "_pressed", at_list=[globals()['{}_pos'.format(button_number)]], zorder=100, layer='screens')
                else:
                    return
            elif ev.type == pygame.MOUSEBUTTONUP and ev.button == LEFT:
                #hide the image when the left mouse button goes back up.
                renpy.hide(store.button_number + "_pressed", layer='screens')
                return
            return

        # Return a small empty render, so we get events.
        def render(self, width, height, st, at):
            return renpy.Render(1, 1)


    # Create a ButtonListener to actually listen for button presses.
    store.button_listener = ButtonListener()

    # This adds button_listener to each interaction.
    def button_overlay():
        ui.add(store.button_listener)

    config.overlay_functions.append(button_overlay)

# screen button_screen:
#     vbox:
#         #doesn't have to be a vbox, but it has to be a container that can use the transform
#         at button1_pos
#         imagebutton:
#             auto "images/button1_%s.png"
#             focus_mask True
#             action Notify("You clicked the button.")
#             alternate Notify("You right-clicked the button.")
#             #use the hovered action to set "button_number" to the name of the button
#             hovered [Notify("You hovered the button."), SetVariable("button_number", "button1")]
#             #use the unhovered action to set "button_number" back to "button0".
#             unhovered [Notify("You unhovered the button."), SetVariable("button_number", "button0")]
#     vbox:
#         at button2_pos
#         imagebutton:
#             auto "images/button2_%s.png"
#             focus_mask True
#             action Notify("You clicked the button.")
#             alternate Notify("You right-clicked the button.")
#             hovered [Notify("You hovered the button."), SetVariable("button_number", "button2")]
#             unhovered [Notify("You unhovered the button."), SetVariable("button_number", "button0")]
