def resolution_with_subsumption(clauses: list[list], alpha: int) -> bool:
    #     Candidates:= clauses U (not alpha)  // append negation of alpha to candidates
    #     Processed = list
    #
    #     while Candidates is not empty {
    #         next candidate:
    #         Next:= Candidates.pop() // remove from list
    #         foreach p in Processed {
    #             if p subsumes Next { // literals in p are a subset of Next
    #                 go to next candidate
    #             }
    #         }
    #
    #         foreach p in Processed {
    #             Resolvents:= resolve(Next, p)
    #             foreach r in Resolvents {
    #                 if r is the empty clause {
    #                     return True
    #                 }
    #                 Candidates.push(r)  // append resolvents to candidates
    #             }
    #         }
    #         Processed.push(Next) // we're done with this clause
    #     }
    #     return False   // alpha is not entailed by clauses
    # }
    processed = []
    candidates = []  # TODO append negation of alpha to candidates
    while not len(candidates) == 0:
        candidate = candidates[0]
        del candidates[0]
        for p in processed:
            if p:  # subsumes Next
                # go to next
                pass

        for p in processed:
            resolvents = []  # resolve(next, p)
            for r in resolvents:
                if r:  # is the empty clause
                    return True
                candidates.append(r)
        processed.append(next)

    return False

def resolution(kb, alpha):
    # kb - teadmusbaas CNF kujul
    # alpha - literaal, mida tahame kontrollida.
    pass
