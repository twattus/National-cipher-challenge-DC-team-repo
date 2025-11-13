ciphertext="""REDMAYMRNIOALOYNATKHOOROUYFUETERTLRRFDAONYCERONUONGAUIRGNPSROESREFEAIIEYATBMAETTLLIWEELHBIFAIEOCRNDVOPIREETRFHURIETMRAAOROLYFUUYDAONRBLLCAOOSOTRRATSREOUPEHITBTUITHTNAKTUERHPETOOIANTFPIETRHRTNEOIGOHDNRTAEUIVOOBSCRTAATTSONIFOUVNACOHEVNNLOIAINOTMIGNEBHETOPTHUOGEEAURDSTTOMHFEHELAEUVOVINFNAETEMSNTIIEENDDFRYETAHENEUTIRTERIHDESOTEIORBHNITTAIRTASEMINHTAELITNITKHHLIWELYRIGOENCZTAHETTHYMEEARBRHTEEOSEAOWRHALWOLISLBTGIONITRODIFTFAIOMOOOFONYDUSADAMNTDALIRLEOYLNHTPATGIHNTCACWNEONOTMAEAENARGRMATTEHNTULLWSIIALLTPARNSETIICGIDLNUDDUOILWOGBYNELTUYTHOARETRPNARTNOSODHMTGIONAATIKHERRFRDOEMMCOEOTPYETLMEPTOTAFRHGABIRSAMRIIENAROYIUNSRLUTYROTMSKIEH"""
#formatting be damned that's all going on one line


sequence_length=3 #looking to candidates for "the"

tree_letter_combos=[]

tree_letter_freqs=[]
tick=0
for e in range(0,len(ciphertext)-sequence_length): #looks for all the 3 letter segments present
    trois_letre_thingy=ciphertext[e:e+sequence_length]
    if trois_letre_thingy not in tree_letter_combos:
        tree_letter_combos.append(trois_letre_thingy) #list of unique thingys
        tree_letter_freqs.append([0,tick]) #must be 2d list for sorting reasons
        tick+=1
    tree_letter_freqs[tree_letter_combos.index(trois_letre_thingy)][0]+=1 #on further consideration it might have been easier just to have made tree_letter_combos 2d and just got rid of tree_letter_freqs


def sort_key(item):
    return item[0]

tree_letter_freqs.sort(key=sort_key,reverse=True)

possibilities_list=[]

for e in range(0,len(tree_letter_freqs)):
    possibilities_list.append([tree_letter_combos[tree_letter_freqs[e][1]],tree_letter_freqs[e][0]])

print(possibilities_list) #sorted in order of frequency