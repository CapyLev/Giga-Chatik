export type isOptionalString = string | undefined;

export interface ModalProps {
  closeModal: () => void;
}

export interface AuthValidationState {
  validationError: string[] | null;
}
