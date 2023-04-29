import math
flag=[84703294725430033906832250067964196205139160156250000000000000000000000000000000000000000000000000000000000000000000000, 45676705824421939478649912270404151469078478270110281072883411705893337269021799922410000000000000000000000000000000000000000000000000000000000000000000000000000, 7553267519536856206894835544419799566515605813936797712534128285594784443588284718339107775974046961403408687562020731652321787481770188797032392344322793, 12302064898724710532827150598154059319480431430194019567533837617701744247540837, 29230373417303981523991743213445438361273460435536387578823301151073955230191893879327166313683698884977174647200661834981895420031938201501844186139312262728596441523234685247298254354510280986013791766000644435467836768083316201227717101573944091796875, 2507595563850434784785830337996672675669560604125169997153806458620432966690565526511489766179145877923915738006635987934121836837641156598216975250418599640557742843596219716091087469160204451859801747081238719457680583, 43011648982582635319441634885912142760291550371422984842327317509027346755941747979492406958501028343730193285796910499406374799475501689378673382234203715968091063791828119752826949520739695435571426839492283983181683622343266533376, 338409674705212417609691900649852521476345945170851409041929587916800000000000000000000000000000000000000000000000000000, 5838413276360385181591767028391056883773971655945411999717209362629772986908587679756966542091219630089064981519262625107710702211640713753452048719903909150541476691387288155965507030487060546875, 36893488147419103232, 13502254696946564495173806638175911781507693442801145274330526912663998013367727307029015641024025066259296175308988463096511282991544425244927962245905501088755549985877751618176086220285258558878857690087424, 5806215119817266890514064687574163450096056773241254504134521339819200993256157721713661766915846752073893526699723474503482135742948819614414876286864326656, 3864537523017258344695351890931987344298927329706434998657235251451519142289560424536193766581922577962463616031502177177365078661042987655742908673467080748696980814823424, 18646113417161314493261616803956698971446415858248583415929120740302154318206422517221824801, 7686497164992228299627380562916545929101608700543543065585889101306502804668416, 1771488381578834144002847499042345499233030965956748369294743421801642321834218646893759465933674268875891603023178802948001446988369, 271050543121376108501863200217485427856445312500000000000000000000000000000000000000000000000000000000000000000, 9762075518152546562417403479355309620079717417407010775401060266867242691438981607825378922831482931561108394891748548182365289000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 65611842679940078030622942156630970663923986079606382810792177516483686301240799777322916195291391059572178488673744694536169438421429070155290749051275090783913021270524713, 3725989217506060809913745704292352543926459628485989232909583897978821195955532381542525335761, 20538815647338713890163745581944536697181476773109383145966227825905854507995909679853031672466883301676933099993306223464877223303799437259685753819540758179913164590356237405865957867945326142944395542144775390625, 97379222408068953807301859267067107189365341269163476237041166966873766956444151001700046478913208416080274157903672383465261657605398327794760445958763463, 100440019470877833693301476035452101140523810378780812530385809310741467786094393086209213809989962019805930526039995867618156970698855949970414255129453454858464793364492687624732646010002214021470148945248636568462163968, 577341790856510457111558003724287890162217584561174978484826825686660447138972158832550595601435202027905724789789745479680000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 8309096452436980233740137520226765924927348021031110314429991625106773198406758301623595724157403340073368535479608203839903083416912671983062770588311512221480235706322957659938841149099898763553950775673229145468212664127349853515625, 2251799813685248, 561031512278819431146795040598417437044790282491383256233876686095187065810146745730996293474876084971026983150796029114532335447326079959019111074361373204831340840605593718751232, 69260929262310627579192861447517452726956512255094630796072906358906254379527149373337720354729667260470872810062056869890321501847580318512698465897081376217525538619130339834658128732884091706351184609629241867977340475321931005952, 2521728396569246669585858566409191283525103313309788586748690777871726193375821479130513040312634601011624191379636224, 15355876181909280421724151687580911741041895655149613132104515881830657073678671819100413262089943, 7207320829241292418372806787841890422340428690648047725581553438112287067299050434183810263512112572730416062823718609946156816522709750226799219120431155876486999101578795151982711974691155889618944, 104300349542165701146018101937616046621361339705427605147181672670062744718838977390700163944299572342492798894460440061371051890236318980386628668903961551927542909085661502464402131320602565654764869975620633428140593908631798363597750002056362174080350852773120561622468109630297204751249]
ha = "32 82 e9 0d 73 67 d4 b4 73 02 4e ca 40 07 2c d1".split(' ') # хэш-сумма MD5 от строки "qwerty21"
for i in range(len(flag)):
    print(chr(round(math.log(flag[i],int('0x'+ha[i%16],16)))),end='')